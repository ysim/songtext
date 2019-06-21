from lxml import html, etree
from lxml.html.clean import clean_html
import requests

from libsongtext.errors import ArgumentError, SearchError
from libsongtext.utils import format_song_info, output_song


API_URL = 'http://lyrics.wikia.com/api.php'
SEARCH_PARAMETERS = {
    'artist': 'artist',
    'title': 'song',
}


class LyricWikiSong(object):

    PARAMS = {
        'fmt': 'realjson',
        'func': 'getSong'
    }
    CSS_SELECTOR = '.lyricbox'

    def __init__(self, args):
        self.args = args

        request_params = self.PARAMS.copy()
        for k, v in SEARCH_PARAMETERS.items():
            if self.args[k] is None:
                print(
                    '\nThis API requires that you search with both the artist '
                    'name (-a, --artist) and the song title (-t, --title). '
                    'All other options will be ignored.\n\n'
                )
                raise ArgumentError
            request_params[v] = self.args[k]

        self.response = requests.get(API_URL, params=request_params)
        self.json = self.response.json()
        if not self.json['page_id']:
            print("\nYour query did not match any tracks.\n\n")
            raise SearchError

        self.url = self.json['url']

    def get_lyrics(self):
        response = requests.get(self.url)
        page_html =  html.document_fromstring(response.text)
        element = page_html.cssselect(self.CSS_SELECTOR)[0]

        # Replace <br> tags with \n (prepend it with \n and then remove all
        # occurrences of <br>)
        for br in element.cssselect('br'):
            br.tail = '\n' + br.tail if br.tail else '\n'
        etree.strip_elements(element, 'br', with_tail=False)

        # Remove unneeded tags
        bad_tags = element.cssselect('.rtMatcher') + \
            element.cssselect('.lyricsbreak')
        for tag in bad_tags:
            tag.drop_tree()

        # Remove HTML comments
        real_string = etree.tostring(element, encoding=unicode)
        cleaned_html = clean_html(real_string)

        info_output = format_song_info(self.json['artist'], self.json['song'])
        lyric_output = html.fragment_fromstring(cleaned_html).text_content()

        return u'{}{}'.format(info_output, lyric_output)


def get_result(args):
    track = LyricWikiSong(args)
    output_song(track.get_lyrics(), args['no_pager'])
