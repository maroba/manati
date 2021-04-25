import unittest
from os.path import exists
import pathlib
import os

from click.testing import CliRunner

from manati.manati import cli


class TestCreate(unittest.TestCase):

    def test_create_project(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ['create', '-n' , 'tee'])
            assert not result.exception

            path = pathlib.Path('tee')
            result = os.system('cd tee; python setup.py develop; python -m unittest discover tests')

            assert exists(path)
            assert exists(path / 'tee')
            assert exists(path /'tee' / '__init__.py')
            assert exists(path / 'setup.py')
            assert result == 0
