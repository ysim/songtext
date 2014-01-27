# LYRICSnMUSIC API wrapper
# Documentation: http://www.lyricsnmusic.com/api

import os

import requests

from base import BaseTrack, BaseTrackList


API_URL = 'http://api.lyricsnmusic.com/songs'
try:
    API_KEY = os.environ['LYRICSNMUSIC_API_KEY']
except KeyError:
    print
    print "You must have the LYRICSNMUSIC_API_KEY environment variable set."
    print "If you don't have an API key, you can get one from here:"
    print
    print "\thttp://www.lyricsnmusic.com/api_keys/new\n"
    raise

SEARCH_PARAMETERS = {
    'query': 'q',
    'artist': 'artist',
    'title': 'track',
    'words': 'lyrics',
}


class Track(BaseTrack):

    CSS_SELECTOR = "pre[itemprop='description']"

    def get_lyrics(self):
        print u'{0}\n\n'.format(self.element.text_content())
        return 0


class TrackList(BaseTrackList):

    def get_response(self, args):
        params = { 'api_key': API_KEY }
        for arg in SEARCH_PARAMETERS.keys():
            if args[arg] is not None:
                params[SEARCH_PARAMETERS[arg]] = args[arg]
        response = requests.get(API_URL, params=params)
        return response

    @property
    def count(self):
        return len(self.json)

    def is_valid(self):
        if self.count == 0:
            print "\nNo tracks matching your query were found.\n\n"
            return False
        print '\n{0} track(s) matched your search query.\n\n'.format(self.count)
        return True

    def get_track_url(self, index=0):
        return self.json[index]['url']

    def get_info(self, index=0):
        output = ""
        line1 = u'{0}: {1}\n'.format(
            self.json[index]['artist']['name'],
            self.json[index]['title']
        )
        line2 = "{0}\n".format("-" * len(line1))
        output += line1
        output += line2
        return output

    def is_track_viewable(self, index):
        is_viewable = self.json[index]['viewable']
        if not is_viewable:
            print 'The requested track is not viewable.\n'
            return False
        return True

    def get_list(self, limit):
        output = 'Displaying the top {0} matches:\n\n'.format(limit)
        for index, track in enumerate(self.json[:limit]):
            viewable = track['viewable']
            line = u'{0:>3}. {1}: {2}'.format(
                index,
                track['artist']['name'],
                track['title'],
            )
            if viewable:
                line += u'\n     ("{0}"...)\n'.format(track['snippet'].splitlines()[0].strip())
            else:
                line += u' (full lyrics unavailable)\n'
            output += line
        print output
        return 0


def get_result(args):
    tracklist = TrackList(args)
    if not tracklist.is_valid():
        return 1
    if args['limit'] is not None:
        return tracklist.get_list(args['limit'])
    if not tracklist.is_track_viewable(args['index']):
        return 1
    track = Track(tracklist.get_track_url(args['index']))
    print tracklist.get_info(int(args['index']))
    return track.get_lyrics()
