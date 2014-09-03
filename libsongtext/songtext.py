#!/usr/bin/env python

####################################
#                                  #
# songtext                         #
# --------                         #
# Song lyrics in the command line! #
#                                  #
####################################

import argparse
from importlib import import_module  # __import__ does not resolve dotted paths
import os
import sys

from .properties import __version__


DEFAULT_API = os.environ.get('SONGTEXT_DEFAULT_API', 'lyricwiki')


def process_args(args):
    if args.pop('version'):
        print '%s.%s.%s' % __version__
        return 0
    get_song_lyrics(args)


def get_song_lyrics(args):
    api = import_module(__package__ + '.' + ''.join(args.pop('api')))

    for arg in getattr(api, 'SEARCH_PARAMETERS').keys():
        if args[arg] is not None:
            args[arg] = ' '.join(args[arg])

    return getattr(api, 'get_result')(args)


def get_parser():
    parser = argparse.ArgumentParser(description='a command line song lyric '
        'fetcher')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*',
        help='Search all fields (artist name, song title, words in lyrics), '
        'e.g. "daft punk get lucky"')
    parser.add_argument('-l', '--list', metavar='N', type=int,
        const=10, nargs='?', dest='limit', help='List the top N matches for '
        'your search query along with a snippet from the lyrics if possible '
        '(defaults to 10)')
    parser.add_argument('-i', '--index', metavar='INDEX', type=int, default=0,
        help='Display the lyrics for match number INDEX (from the list when '
        'running the same search query with the --list option)')
    parser.add_argument('-a', '--artist', metavar='ARTIST_NAME', type=str,
        nargs='+')
    parser.add_argument('-t', '--title', metavar='SONG_TITLE', type=str,
        nargs='+')
    parser.add_argument('-w', '--words', metavar='LYRICS', type=str,
        nargs='+')
    parser.add_argument('--api', metavar='API_MODULE', type=str, nargs=1,
        default=DEFAULT_API)
    parser.add_argument('-V', '--version', action='store_true')
    return parser


def main():
    parser = get_parser()
    if not len(sys.argv) > 1:
        parser.print_help()
        return 1
    args = vars(parser.parse_args())
    return process_args(args)
