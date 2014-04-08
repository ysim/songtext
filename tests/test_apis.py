#!/usr/bin/env python

import unittest

from .context import songtext


class LyricsNMusicTests(unittest.TestCase):

    def get_args(self, arg_string):
        arg_string += ' --api lyricsnmusic'
        parser = songtext.get_parser()
        args = vars(parser.parse_args(arg_string.split(' ')))
        return args

    def test_get_single_result_with_artist_and_song_title(self):
        arg_dict = self.get_args('-a johnny flynn -t the box')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 0)

    def test_get_single_result_with_artist_only(self):
        arg_dict = self.get_args('-a laura marling')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 0)

    def test_get_single_result_with_song_title_only(self):
        arg_dict = self.get_args('-t lillian egypt')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 0)

    def test_get_single_result_with_words_only(self):
        arg_dict = self.get_args('-w all the rowboats in the paintings')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 0)

    def test_get_list_result_with_artist_and_song_title(self):
        arg_dict = self.get_args('-a the xx -t infinity -l')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 0)

    def test_get_list_result_with_artist_only(self):
        arg_dict = self.get_args('-a yeah yeah yeahs -l')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 0)

    def test_get_list_result_with_song_title_only(self):
        arg_dict = self.get_args('-t gimme sympathy')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 0)

    def test_get_list_result_with_words_only(self):
        arg_dict = self.get_args('-w i see a red door and i want it painted '
            'black -l')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 0)


class LyricWikiTests(unittest.TestCase):

    def get_args(self, arg_string):
        arg_string += ' --api lyricwiki'
        parser = songtext.get_parser()
        args = vars(parser.parse_args(arg_string.split(' ')))
        return args

    def test_get_single_result_with_artist_and_song_title(self):
        arg_dict = self.get_args('-a mumford and sons -t the cave')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 0)

    def test_searching_with_list_option_fails(self):
        arg_dict = self.get_args('-a josh rouse -l')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 1)

    def test_searching_with_words_option_fails(self):
        arg_dict = self.get_args('-w home is wherever i\'m with you')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 1)

    def test_searching_with_artist_only_fails(self):
        arg_dict = self.get_args('-a arcade fire')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 1)

    def test_searching_with_song_title_only_fails(self):
        arg_dict = self.get_args('-t stairway to heaven')
        ret_value = songtext.get_song_lyrics(arg_dict)
        self.assertEqual(ret_value, 1)


if __name__ == '__main__':
    unittest.main()
