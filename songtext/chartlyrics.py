# ChartLyrics API wrapper
# Documentation: http://www.chartlyrics.com/api.aspx

from xml.dom.minidom import parseString

import requests


API_URL = 'http://api.chartlyrics.com/apiv1.asmx/'

API_METHODS = {
    'SearchLyric': {
        'params': ['artist', 'song'],
        'description': 'Returns an ArrayOfSearchLyricResult of matching tracks '
            'given both an artist and song title',
    },
    'SearchLyricDirect': {
        'params': ['artist', 'song'],
        'description': 'Returns the top match for the search query',
    },
    'SearchLyricText': {
        'params': ['lyricText'],
        'description': 'Returns an ArrayOfSearchLyricResult of matching '
            'tracks given a snippet of the lyric text',
    },
    'GetLyric': {
        'params': ['lyricId', 'lyricCheckSum'],
        'description': 'Returns the song lyrics given an ID and checksum',
    },
    'AddLyric': {  # Not supported
        'params': ['trackId', 'trackCheckSum', 'lyric', 'email'],
        'description': 'Add lyrics for a song',
    },
}

SEARCH_PARAMETERS = {
    'artist': 'artist',
    'title': 'song',
    'words': 'lyricText',
}


class Track(object):

    def __init__(self, args):
        self.args = args
        self.response = self.get_response(args)
        self.xml_doc = parseString(self.response.content)

    def get_response(self, args):
        params = {}
        if 'lyricId' in args and 'lyricCheckSum' in args:
            params = args
            method = 'GetLyric'
        else:
            for arg in SEARCH_PARAMETERS.keys():
                if arg in args and args[arg] is not None:
                    params[SEARCH_PARAMETERS[arg]] = args[arg]
            search_params = params.keys()
            if 'artist' in search_params and 'song' in search_params:
                method = 'SearchLyricDirect'
            else:
                raise Exception('You need either the lyricId and lyricCheckSum '
                    'parameters for the GetLyric method or the artist and song '
                    'parameters for the SearchLyricDirect method.')
        url = API_URL + method
        response = requests.get(url, params=params)
        return response

    def is_valid(self):
        if self.xml_doc.getElementsByTagName('LyricId')[0].firstChild.nodeValue == u'0':
            print u'\nThe requested lyrics are not available.\n\n'
            return False
        return True

    def get_info(self):
        output = ""
        artist = self.xml_doc.getElementsByTagName('LyricArtist')[0].firstChild.nodeValue
        title = self.xml_doc.getElementsByTagName('LyricSong')[0].firstChild.nodeValue
        line1 = u'\n{0}: {1}\n'.format(artist, title)
        line2 = '{0}\n'.format('-' * len(line1))
        output += line1
        output += line2
        return output

    @property
    def element(self):
        return self.xml_doc.getElementsByTagName('Lyric')[0]

    def get_lyrics(self):
        print self.get_info()
        print u'{0}\n\n'.format(self.element.firstChild.nodeValue)
        return 0


class TrackList(object):

    def __init__(self, args):
        self.args = args
        self.response = self.get_response(args)
        self.xml_doc = parseString(self.response.content)

    def get_response(self, args):
        params = {}
        for arg in SEARCH_PARAMETERS.keys():
            if args[arg] is not None:
                params[SEARCH_PARAMETERS[arg]] = args[arg]
        search_params = params.keys()
        if 'lyricText' in search_params:
            method = 'SearchLyricText'
        elif 'artist' in search_params and 'song' in search_params:
            method = 'SearchLyric'
        else:
            raise Exception('You specify either the lyric text (-w, --words) '
                'or both the artist name (-a, --artist) and song title (-t, '
                '--title) to be able to search this API.')
        url = API_URL + method
        response = requests.get(url, params=params)
        return response

    @property
    def count(self):
        return len(self.get_cleaned_results())

    def get_cleaned_results(self):
        """ Remove all the empty <SearchLyricResult> tags. """
        raw_results = self.xml_doc.getElementsByTagName('SearchLyricResult')
        return [result_element for result_element in raw_results \
            if not result_element.hasAttribute('xsi:nil')]
        
    def is_valid(self):
        if self.count == 0:
            print "\nNo tracks matching your query were found.\n\n"
            return False
        print '\n{0} track(s) matched your search query.\n\n'.format(self.count)
        return True

    def get_list(self, limit):
        output = 'Displaying the top {0} matches:\n\n'.format(limit)
        if limit > self.count:
            limit = self.count
        for index, node in enumerate(self.get_cleaned_results()[:limit]):
            line = u'{0:>3}. {1}: {2}\n'.format(
                index,
                node.getElementsByTagName('Artist')[0].firstChild.nodeValue,
                node.getElementsByTagName('Song')[0].firstChild.nodeValue,
            )
            output += line
        print output
        return 0

    def get_id_and_checksum(self, index):
        element = self.get_cleaned_results()[index]
        try:
            lyric_id = element.getElementsByTagName('LyricId')[0].firstChild.nodeValue
            lyric_checksum = element.getElementsByTagName('LyricChecksum')[0].firstChild.nodeValue
        except IndexError:
            print "\nThe selected match has no lyrics.\n\n"
            raise
        return { 'lyricId': lyric_id, 'lyricCheckSum': lyric_checksum }


def get_result(args):
    print args
    if args['limit'] is None and args['index'] == 0:
        track = Track(args)
        if not track.is_valid():
            return 1
        return track.get_lyrics()
    tracklist = TrackList(args)
    if not tracklist.is_valid():
        return 1
    if args['index'] != 0:
        track = Track(tracklist.get_id_and_checksum(args['index']))
        return track.get_lyrics()
    return tracklist.get_list(args['limit'])
