import sys
import os

from lxml import html
import requests


API_URL = 'http://api.lyricsnmusic.com/songs'
try:
    API_KEY = os.environ['LYRICSNMUSIC_API_KEY']
except KeyError:
    print
    print "You must have the LYRICSNMUSIC_API_KEY environment variable set."
    print "If you don't have an API key, you can get one from here:"
    print
    print "\thttp://www.lyricsnmusic.com/api_keys/new"
    print
    sys.exit(1)
CSS_SELECTOR = "pre[itemprop='description']"


class Track(object):

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)

    @property
    def html_string(self):
        return html.document_fromstring(self.response.text)

    def get_lyrics(self):
        try:
            return self.html_string.cssselect(CSS_SELECTOR)[0].text_content()
        except IndexError:
            print
            print "Lyrics could not be fetched. For more details, go to:"
            print
            print "\t{0}".format(self.url)
            return ""


class TrackList(object):

    def __init__(self, query=None):
        self.query = query
        self.response = self.get_response(query)
        self.json = self.response.json()

    def get_response(self, query=None):
        params = { 'api_key': API_KEY, 'q': query }
        response = requests.get(API_URL, params=params)
        return response

    @property
    def count(self):
        return len(self.json)

    def get_track_url(self, index=0):
        return self.json[index]['url']

    def get_list(self, limit=10):
        output = ""
        for index, track in enumerate(self.json[:limit]):
            line1 = u'{0:>3}. {1}: {2}\n'.format(
                index,
                track['artist']['name'],
                track['title'],
            )
            line2 = u'     ("{0}"...)\n'.format(track['snippet'].splitlines()[0].strip())
            output += line1
            output += line2
        return output


def check_matches(tracklist_object):
    count = tracklist_object.count
    if count == 0:
        print
        print "No tracks matching your query were found."
        print
        sys.exit(1)
    print "{0} track(s) matched your search query.\n".format(count)


def get_first_track(query):
    track_list = TrackList(query)
    check_matches(track_list)
    track = Track(track_list.get_track_url())
    print track.get_lyrics()


def get_track_list(query, limit):
    track_list = TrackList(query)
    check_matches(track_list)
    print track_list.get_list(limit)
