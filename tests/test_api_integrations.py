import click
from click.testing import CliRunner

from .context import errors, songtext


runner = CliRunner()


class TestLyricWiki:

    def test_get_single_result_with_artist_and_song_title(self):
        result = runner.invoke(songtext.cli, [
            '-a', 'Paramore',
            '-t', 'Where the Lines Overlap',
            '--no-pager'
        ])
        assert result.exit_code == 0
        assert 'Paramore: Where The Lines Overlap' in result.output

    def test_error_with_artist_only(self):
        result = runner.invoke(songtext.cli, ['-a', 'Die Antwoord'])
        assert isinstance(result.exception, errors.ArgumentError)

    def test_error_with_song_title_only(self):
        result = runner.invoke(songtext.cli, ['-t', 'get lucky'])
        assert isinstance(result.exception, errors.ArgumentError)

    def test_searching_with_positional_arguments_fails(self):
        result = runner.invoke(songtext.cli, ['joy division atmosphere'])
        assert isinstance(result.exception, errors.ArgumentError)

    def test_searching_with_words_option_fails(self):
        result = runner.invoke(songtext.cli, ['-w', 'you want a bugatti'])
        assert isinstance(result.exception, errors.ArgumentError)


class TestLyricsNMusic:

    def test_get_single_result_with_artist_and_song_title(self):
        result = runner.invoke(songtext.cli, [
            '--api', 'lyricsnmusic',
            '-a', 'Tove Lo',
            '-t', 'Talking Body'
        ])
        assert result.exit_code == 0
        assert 'Tove Lo: Talking Body' in result.output

    def test_get_single_result_with_words(self):
        result = runner.invoke(songtext.cli, [
            '--api', 'lyricsnmusic',
            '-w', 'two hearts fading',
            '--no-pager'
        ])
        assert result.exit_code == 0
        assert 'Ryan Adams: Desire' in result.output

    def test_get_list_with_artist_and_song_title(self):
        result = runner.invoke(songtext.cli, [
            '--api', 'lyricsnmusic',
            '-a', 'David Bowie',
            '-t', 'Heroes'
        ])
        assert result.exit_code == 0
        assert 'David Bowie: Heroes' in result.output

    def test_get_list_with_limit_of_20(self):
        result = runner.invoke(songtext.cli, [
            '--api', 'lyricsnmusic',
            'love', '-l', '--limit', '20'
        ])
        assert result.exit_code == 0
        assert '19.' in result.output
        assert 'Displaying the top' in result.output

    def test_get_list_with_only_limit_option_specified(self):
        """
        You should still get a list back even if you only specify --limit
        and not -l/--show-list
        """
        result = runner.invoke(songtext.cli, [
            '--api', 'lyricsnmusic',
            '-a', 'Rob Thomas',
            '-t' 'This is How a Heart Breaks',
            '--limit', '5'
        ])
        assert result.exit_code == 0
        assert '0.' in result.output
        assert 'Displaying the top' in result.output

    def test_get_song_with_index(self):
        result = runner.invoke(songtext.cli, [
            '--api', 'lyricsnmusic',
            '-a', 'Kiesza',
            '-t', 'Hideaway',
            '-i', '1',
            '--no-pager'
        ])
        assert result.exit_code == 0
        assert 'Kiesza: Hideaway' in result.output

    def test_error_on_out_of_range_index(sel):
        result = runner.invoke(songtext.cli, [
            '--api', 'lyricsnmusic',
            '-a', 'Eminem',
            '-t', 'Lose Yourself',
            '-i', '30'
        ])
        assert 'out of range' in result.output
        assert isinstance(result.exception, errors.TrackIndexError)

    def test_get_list_with_artist_only(self):
        result = runner.invoke(songtext.cli, [
            '--api', 'lyricsnmusic',
            '-a', 'Zara Larsson',
            '-l'
        ])
        assert result.exit_code == 0
        assert 'Displaying the top' in result.output

    def test_get_list_with_song_title_only(self):
        result = runner.invoke(songtext.cli, [
            '--api', 'lyricsnmusic',
            '-t', 'Defying Gravity',
            '-l'
        ])
        assert result.exit_code == 0
        assert 'Displaying the top' in result.output
