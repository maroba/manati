import unittest
import os
from pathlib import Path

from click.testing import CliRunner

from manati.create import create_project
from manati.manati import cli


class TestInfo(unittest.TestCase):

    def test_info(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            create_project('abc', True, True, 'test_author', 'test_desc', 'MIT')
            os.chdir(Path.cwd() / 'abc')
            result = runner.invoke(cli, ['info'])
            assert result.exit_code == 0
            assert 'Package: abc' in result.output
            assert 'Version: 0.0.1' in result.output
            assert 'Author: test_author' in result.output


if __name__ == '__main__':
    unittest.main()
