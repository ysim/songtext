import click
from click.testing import CliRunner

from tests.context import errors, songtext


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
