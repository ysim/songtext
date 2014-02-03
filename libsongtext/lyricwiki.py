# LyricWiki API wrapper
# Documentation: http://api.wikia.com/wiki/LyricWiki_API/REST
#
# Notable points:
# - There is no general search parameter; one can only search by song and
#   artist ('getSong') or only by artist ('getArtist'), which returns the
#   entire discography without any links.

from lxml import html, etree
from lxml.html.clean import clean_html
import requests

from base import BaseTrack, BaseTrackList
from errors import ArgumentError


API_URL = 'http://lyrics.wikia.com/api.php'
SEARCH_PARAMETERS = {
    'artist': 'artist',
    'title': 'song',
}


class Track(BaseTrack):

    CSS_SELECTOR = '.lyricbox'

    def get_lyrics(self):
        element = self.element

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
        print u'{0}'.format(
            html.fragment_fromstring(cleaned_html).text_content()
        )
        return 0


class TrackList(BaseTrackList):

    def get_response(self, args):
        params = { 'fmt': 'realjson' }

        for arg in SEARCH_PARAMETERS.keys():
            if args[arg] is not None:
                params[SEARCH_PARAMETERS[arg]] = args[arg]
        if 'artist' in params and 'song' in params:
            params['func'] = 'getSong'
        else:
            print ('\nThis API requires that you search with both the artist '
                'name (-a, --artist) and the song title (-t, --title).\n\n')
            raise ArgumentError
        response = requests.get(API_URL, params=params)
        return response

    def is_valid(self):
        if not self.json['page_id']:
            print "\nYour query did not match any tracks.\n\n"
            return False
        return True

    def get_track_url(self, index=None):
        if index is not None:
            raise ValueError('This API only returns one result in searches, '
                'therefore it is not possible to specify an index.')
        return self.json['url']

    def get_info(self):
        output = ""
        line1 = u'\n{0}: {1}\n'.format(self.json['artist'], self.json['song'])
        line2 = '{0}\n'.format('-' * len(line1))
        output += line1
        output += line2
        return output


def get_result(args):
    if args['limit'] is not None:
        print ('\nThe list option (-l, --list) is not supported by this API '
            'as it can only return a single match for each search.\n\n')
        return 1
    if args['words'] is not None:
        print ('\nThe words option (-w, --words) is not supported by this API '
            '\n\n.')
        return 1
    try:
        track_list = TrackList(args)
    except ArgumentError:
        return 1
    if not track_list.is_valid():
        return 1
    track = Track(track_list.get_track_url())
    print track_list.get_info()
    return track.get_lyrics()
