import os

from lxml import html
import requests

from errors import SearchError
from utils import format_song_info, output_song


try:
    API_KEY = os.environ['LYRICSNMUSIC_API_KEY']
except KeyError:
    print
    print "You must have the LYRICSNMUSIC_API_KEY environment variable set."
    print "If you don't have an API key, you can get one from here:"
    print
    print "\thttp://www.lyricsnmusic.com/api_keys/new\n"
    raise


API_URL = 'http://api.lyricsnmusic.com/songs'
SEARCH_PARAMETERS = {
    'all_fields': 'q',
    'artist': 'artist',
    'title': 'track',
    'words': 'lyrics',
}


class LNMTrackList(object):

    CSS_SELECTOR = "pre[itemprop='description']"

    def __init__(self, args):
        self.args = args.copy()

        if self.args['limit'] is None:
            self.args['limit'] = 10

        if self.args['index'] is None:
            self.args['index'] = 0

        self.response = self.get_response()
        self.json = self.response.json()

        self.count = len(self.json)
        if self.count == 0:
            print("\nNo tracks matching your query were found.\n\n")
            raise SearchError
        else:
            print("\n{} track(s) matched your search query.\n\n".format(self.count))

    def get_response(self):
        params = { 'api_key': API_KEY }
        for k, v in SEARCH_PARAMETERS.items():
            if self.args[k] is not None:
                params[v] = self.args[k]
        response = requests.get(API_URL, params=params)
        return response

    def get_list(self):
        output = 'Displaying the top {0} matches:\n\n'.format(self.args['limit'])
        for index, track in enumerate(self.json[:self.args['limit']]):
            viewable = track['viewable']
            line = u'{0:>3}. {1}: {2}'.format(
                index,
                track['artist']['name'],
                track['title'],
            )
            if viewable:
                line += u'\n     ("{0}"...)\n'.format(
                    track['snippet'].splitlines()[0].strip()
                )
            else:
                line += u' (full lyrics unavailable)\n'
            output += line
        return output

    def get_lyrics(self):
        track_url = self.json[self.args['index']]['url']
        response = requests.get(track_url)
        page_html = html.document_fromstring(response.text)
        element = page_html.cssselect(self.CSS_SELECTOR)[0]

        info_output = format_song_info(
            self.json[self.args['index']]['artist']['name'],
            self.json[self.args['index']]['title']
        )
        lyric_output = element.text_content()
        return u'{}{}\n\n'.format(info_output, lyric_output)


def get_result(args):
    tracklist = LNMTrackList(args)

    if args['list']:
        print(tracklist.get_list())
        if args['index'] is None:
            return 0

    output_song(tracklist.get_lyrics(), args['no_pager'])
    return 0
