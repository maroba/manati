import unittest
import unittest.mock
from pathlib import Path
import shutil
import os

from click.testing import CliRunner

from manati.create import create_project_structure, create_docs
from manati.manati import cli
from manati.utils import shell


class TestRun(unittest.TestCase):

    def test_run_tests(self):
        runner = CliRunner()
        with runner.isolated_filesystem() as fs:
            create_project_structure('test_project', Path('test_project'), {'PROJECT_NAME': 'test_project',
                                                                                    'MODULE_NAME': 'test_project'})

            os.chdir(Path.cwd() / 'test_project')
            shell('pip install -e .')
            result = runner.invoke(cli, ['run', 'tests', '-r', 'unittest', '-t', 'tests'])
            assert result.exit_code == 0

            result = runner.invoke(cli, ['run', 'tests', '-r', 'pytest', '-t', 'tests'])
            assert result.exit_code == 0

    def test_run_coverage(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            create_project_structure('test_project', Path('test_project'), {'PROJECT_NAME': 'test_project',
                                                                                    'MODULE_NAME': 'test_project'})
            os.chdir(Path.cwd() / 'test_project')
            shell('pip install -e .')

            result = runner.invoke(cli, ['run', 'coverage', '-r', 'unittest', '-s', 'test_project', '-t', 'tests'])
            assert result.exit_code == 0

            result = runner.invoke(cli, ['run', 'coverage', '-r', 'pytest', '-s', 'test_project', '-t', 'tests'])
            assert result.exit_code == 0

    @unittest.mock.patch('manati.run.click.launch')
    def test_run_docs(self, mock_launch):
        runner = CliRunner()
        with runner.isolated_filesystem():
            create_docs(Path.cwd(), 'name_of_project', 'test_author')
            shutil.rmtree(Path.cwd() / 'docs' / '_build')
            result = runner.invoke(cli, ['run', 'docs'])
            assert result.exit_code == 0
            assert os.path.exists(Path.cwd() / 'docs' / '_build' / 'html' / 'index.html')
