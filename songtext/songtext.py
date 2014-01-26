#!/usr/bin/env python

####################################
#                                  #
# songtext                         #
# --------                         #
# Song lyrics in the command line! #
#                                  #
####################################

import argparse
import sys

import lyricsnmusic


def get_song_lyrics(args):
    for arg in lyricsnmusic.SEARCH_PARAMETERS.keys():
        if args[arg] is not None:
            args[arg] = ' '.join(args[arg])

    if args['limit'] is not None:
        return lyricsnmusic.get_track_list(args)

    return lyricsnmusic.get_track(args)


def get_parser():
    parser = argparse.ArgumentParser(description='grab some song lyrics')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*',
        help='search all fields (artist name, song title, words in lyrics), '
        'e.g. "daft punk get lucky"')
    parser.add_argument('-l', '--list', metavar='NUM_MATCHES', type=int,
        const=10, nargs='?', dest='limit', help='list the first n matches '
        'along with a snippet from the lyrics')
    parser.add_argument('-i', '--index', dest='index', type=int, default=0)
    parser.add_argument('-a', '--artist', metavar='ARTIST_NAME', type=str,
        nargs='+')
    parser.add_argument('-t', '--title', metavar='SONG_TITLE', type=str,
        nargs='+')
    parser.add_argument('-w', '--words', metavar='LYRICS', type=str,
        nargs='+')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    return get_song_lyrics(args)


if __name__ == '__main__':
    sys.exit(main())
