# LyricWiki API wrapper
# Documentation: http://api.wikia.com/wiki/LyricWiki_API/REST
#
# Notable points:
# - There is no general search parameter; one can only search by song and
#   artist ('getSong') or only by artist ('getArtist'), which returns the
#   entire discography without any links.

from pydoc import pager

from lxml import html, etree
from lxml.html.clean import clean_html
import requests

from errors import ArgumentError, SearchError


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

        for search_param in SEARCH_PARAMETERS.keys():
            if search_param is None:
                print(
                    '\nThis API requires that you search with both the artist '
                    'name (-a, --artist) and the song title (-t, --title).\n\n'
                )
                raise ArgumentError

        # Check if query matched any tracks
        request_params = args.copy()
        request_params.update(self.PARAMS)
        self.response = requests.get(API_URL, params=request_params)
        self.json = self.response.json()
        if not self.json['page_id']:
            print("\nYour query did not match any tracks.\n\n")
            raise SearchError

        # Query matched a track
        self.url = self.json['url']

    def get_info(self):
        output = ""
        line1 = u'\n{0}: {1}\n'.format(self.json['artist'], self.json['song'])
        line2 = '{0}\n'.format('-' * len(line1))
        output += line1
        output += line2
        return output

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
        return u'{0}'.format(
            html.fragment_fromstring(cleaned_html).text_content()
        )


def get_result(args):
    if args['limit'] is not None:
        print(
            '\nThe list option (-l, --list) is not supported by this API '
            'as it can only return a single match for each search.\n\n'
        )
        return 1
    if args['words'] is not None:
        print(
            '\nThe words option (-w, --words) is not supported by this API '
            '\n\n.'
        )
        return 1

    try:
        track = LyricWikiSong(args)
    except ArgumentError:
        return 1

    pager(track.get_info() + track.get_lyrics())
    return 0
