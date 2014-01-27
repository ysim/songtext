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
        try:
            print u'{0}\n\n'.format(
                self.html_element.cssselect(self.CSS_SELECTOR)[0].text_content()
            )
            return 0
        except IndexError:
            print
            print "Lyrics could not be fetched. For more details, go to:"
            print
            print "\t{0}".format(self.url)
            return 1


class TrackList(BaseTrackList):

    def get_response(self, args):
        params = { 'api_key': API_KEY }
        for arg in SEARCH_PARAMETERS.keys():
            if args[arg] is not None:
                params[SEARCH_PARAMETERS[arg]] = args[arg]
        response = requests.get(API_URL, params=params)
        return response

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
        return self.json[index]['viewable']

    def get_list(self, limit=10):
        output = ""
        for index, track in enumerate(self.json[:limit]):
            viewable = track['viewable']
            line = u'{0:>3}. {1}: {2}'.format(
                index,
                track['artist']['name'],
                track['title'],
                track['viewable'],
            )
            if viewable:
                line += u'\n     ("{0}"...)\n'.format(track['snippet'].splitlines()[0].strip())
            else:
                line += u' (full lyrics unavailable)\n'
            output += line
        return output


def check_matches(tracklist_object):
    count = tracklist_object.count
    if count == 0:
        print "\nNo tracks matching your query were found.\n\n"
        return False
    print '\n{0} track(s) matched your search query.\n\n'.format(count)
    return True


def get_track_list(args):
    track_list = TrackList(args)
    if not check_matches(track_list):
        return 1
    print "Displaying the top {0} matches:\n".format(args['limit'])
    print track_list.get_list(args['limit'])
    return 0


def get_track(args):
    track_list = TrackList(args)
    num_matches = check_matches(track_list)
    if not num_matches:
        return 1
    if not track_list.is_track_viewable(args['index']):
        print "The requested track is not viewable."
        print
        return 1
    track = Track(track_list.get_track_url(args['index']))
    print track_list.get_info(int(args['index']))
    return track.get_lyrics()
