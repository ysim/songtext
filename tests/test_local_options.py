import click
from click.testing import CliRunner

from .context import songtext


runner = CliRunner()


class TestGeneral:

    def test_help(self):
        result = runner.invoke(songtext.cli, ['--help'])
        assert result.exit_code == 0

    def test_version(self):
        result = runner.invoke(songtext.cli, ['--version'])
        assert result.exit_code == 0
        assert result.output == '0.1.4\n'
