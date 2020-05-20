import unittest

import click
from click.testing import CliRunner

from tests.context import songtext

runner = CliRunner()

class TestGeneral(unittest.TestCase):

    def test_help(self):
        result = runner.invoke(songtext.cli, ['--help'])
        self.assertEqual(result.exit_code, 0)

    def test_version(self):
        result = runner.invoke(songtext.cli, ['--version'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, '0.1.9\n')
