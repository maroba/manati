import unittest
import unittest.mock
import pathlib
import os

from click.testing import CliRunner

from manati.utils import shell
from manati.manati import cli
from manati.create import create_project_structure


class TestDeploy(unittest.TestCase):

    def test_deploy(self):
        runner = CliRunner()
        with unittest.mock.patch('manati.deploy.do_twine') as mock:
            instance = mock.return_value
            instance.method.return_value = 'OK'

            with runner.isolated_filesystem():
                create_project_structure('test_project', pathlib.Path('test_project'), {'PROJECT_NAME': 'test_project',
                                                                                        'MODULE_NAME': 'test_project'})

                os.chdir(pathlib.Path.cwd() / 'test_project')
                shell('mkdir build dist')
                result = runner.invoke(cli, ['deploy', 'pypi'], input='y\n')
                assert result.exit_code == 0

    def test_deploy_no_overwrite(self):
        runner = CliRunner()
        with unittest.mock.patch('manati.deploy.do_twine') as mock:
            instance = mock.return_value
            instance.method.return_value = 'OK'

            with runner.isolated_filesystem():
                create_project_structure('test_project', pathlib.Path('test_project'), {'PROJECT_NAME': 'test_project',
                                                                                        'MODULE_NAME': 'test_project'})

                os.chdir(pathlib.Path.cwd() / 'test_project')
                shell('mkdir build dist')
                result = runner.invoke(cli, ['deploy', 'pypi'], input='n\n')
                assert result.exit_code == 0
                assert len(os.listdir('build')) == 0


