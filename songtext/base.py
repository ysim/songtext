# Abstract base classes for the API wrappers.

from lxml import html
import requests


class BaseTrack(object):

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)

    @property
    def page_html(self):
        return html.document_fromstring(self.response.text)

    @property
    def element(self):
        """Return the HTML element that contains the lyrics."""
        return self.page_html.cssselect(self.CSS_SELECTOR)[0]

    def get_lyrics(self):
        raise NotImplementedError("""
            This method should perform any needed cleaning, print a unicode
            string of the requested song lyrics and return 0 if successful,
            else 1.
        """)


class BaseTrackList(object):

    def __init__(self, args):
        self.args = args
        self.response = self.get_response(args)
        self.json = self.response.json()

    def get_response(self, args):
        raise NotImplementedError("""
            Build the GET request here with the desired parameters (e.g. the
            API key) and return the response object.
        """)

    def is_valid(self):
        raise NotImplementedError("""Check the result set of the response and
            return True if one or more tracks matched the search query.
        """)

    def get_track_url(self, index):
        raise NotImplementedError('Return the URL of the requested track.')

    def get_info(self, index):
        raise NotImplementedError("""
            Print the meta information of the track, such as the artist name
            and song title.
        """)

    def get_list(self, limit):
        raise NotImplementedError("""
            Return a formatted list of the tracks that matched the search
            query.
        """)
