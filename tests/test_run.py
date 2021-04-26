import unittest
import pathlib
import os

from click.testing import CliRunner

from manati.create import create_project_structure
from manati.manati import cli
from manati.utils import shell


class TestRun(unittest.TestCase):

    def test_run_tests(self):
        runner = CliRunner()
        with runner.isolated_filesystem() as fs:
            create_project_structure('test_project', pathlib.Path('test_project'), {'PROJECT_NAME': 'test_project',
                                                                                    'MODULE_NAME': 'test_project'})

            os.chdir(pathlib.Path.cwd() / 'test_project')
            result = runner.invoke(cli, ['run', 'tests', '-r', 'unittest', '-d', 'tests'])
            assert result.exit_code == 0


    def test_run_coverage(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            create_project_structure('test_project', pathlib.Path('test_project'), {'PROJECT_NAME': 'test_project',
                                                                                    'MODULE_NAME': 'test_project'})
            os.chdir(pathlib.Path.cwd() / 'test_project')
            result = runner.invoke(cli, ['run', 'coverage', '-r', 'unittest', '-s', 'test_project', '-t', 'tests'])
            assert result.exit_code == 0
