#!/usr/bin/env python

####################################
#                                  #
# songtext                         #
# --------                         #
# Song lyrics in the command line! #
#                                  #
####################################

import argparse

import lyricsnmusic


def get_song_lyrics(args):
    query_args = ' '.join(args['query'])
    return lyricsnmusic.get_first_track(query_args)


def get_parser():
    parser = argparse.ArgumentParser(description='grab some song lyrics')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='+',
        help='artist and song title, e.g. "daft punk get lucky"')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    print get_song_lyrics(args)


if __name__=='__main__':
    main()
