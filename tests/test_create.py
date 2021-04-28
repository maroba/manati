import unittest
from os.path import exists
import pathlib

from click.testing import CliRunner

from manati.manati import cli


class TestCreate(unittest.TestCase):

    def test_create_project(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ['create', '-n' , 'tee'])
            assert not result.exception

            path = pathlib.Path('tee')

            assert exists(path)
            assert exists(path / 'tee')
            assert exists(path /'tee' / '__init__.py')
            assert exists(path / 'setup.py')
            assert exists(path / 'docs' / 'conf.py')
            assert exists(path / 'docs' / '_build' / 'html' / 'index.html')

