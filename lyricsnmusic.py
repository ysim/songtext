import sys
import os

from lxml import html
import requests


API_URL = 'http://api.lyricsnmusic.com/songs'
try:
    API_KEY = os.environ['LYRICSNMUSIC_API_KEY']
except KeyError:
    print "You must have the LYRICSNMUSIC_API_KEY environment variable set."
    print "If you don't have one, you can get one from here: "
    print "\thttp://www.lyricsnmusic.com/api_keys/new"
    sys.exit(1)
CSS_SELECTOR = "pre[itemprop='description']"


def get_response(query):
    params = { 'api_key': API_KEY, 'q': query }
    response = requests.get(API_URL, params=params)
    return response


def get_track_url(response):
    json_data = response.json()
    print "{0} track(s) matched your search query.\n".format(len(json_data))
    return json_data[0]['url']


def get_track_lyrics(url):
    track_page_response = requests.get(url)
    track_page_html = html.document_fromstring(track_page_response.text)
    matched_html_elements = track_page_html.cssselect(CSS_SELECTOR)
    return matched_html_elements[0].text_content()


def search(query):
    response = get_response(query)
    track_url = get_track_url(response)
    return get_track_lyrics(track_url)
