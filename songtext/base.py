from lxml import html
import requests


class BaseTrack(object):

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)

    @property
    def html_string(self):
        return html.document_fromstring(self.response.text)

    def get_lyrics(self):
        raise NotImplementedError('This method should return a printable '
            'unicode string of the requested song lyrics.')


class BaseTrackList(object):

    def __init__(self, args):
        self.args = args
        self.response = self.get_response(args)
        self.json = self.response.json()

    def get_response(self, args):
        raise NotImplementedError('Build the GET request here with the '
            'desired parameters (e.g. the API key) and return the response '
            'object.')

    @property
    def count(self):
        return len(self.json)

    def get_track_url(self, index=0):
        raise NotImplementedError('Return the URL of the requested track.')

    def get_info(self, index=0):
        raise NotImplementedError('Print the meta information of the track, '
            'such as the artist name and song title.')

    def get_list(self, limit=10):
        raise NotImplementedError('Return a formatted list of the tracks that '
            'matched the search query.')
