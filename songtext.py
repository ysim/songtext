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
    query_args = ' '.join(args['query'])
    list_arg = args['list']
    index_arg = args['track']

    if list_arg is not None:
        return lyricsnmusic.get_track_list(query_args, list_arg)

    return lyricsnmusic.get_track(query_args, index_arg)


def get_parser():
    parser = argparse.ArgumentParser(description='grab some song lyrics')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*',
        help='artist and song title, e.g. "daft punk get lucky"')
    parser.add_argument('-l', '--list', metavar='NUM_MATCHES', type=int,
        const=10, nargs='?', help='list the first n matches along with a '
        'snippet from the lyrics')
    parser.add_argument('-t', '--track', type=int, default=0)
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    return get_song_lyrics(args)


if __name__ == '__main__':
    sys.exit(main())
