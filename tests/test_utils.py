import unittest
import unittest.mock
import subprocess
import platform

from click.testing import CliRunner

from manati.utils import find_project_data, task


class TestUtils(unittest.TestCase):

    @unittest.mock.patch('manati.utils.shell')
    @unittest.mock.patch('manati.utils.os.environ.get')
    def test_find_project_data_author_from_env(self, mock_env, mock_shell):
        mock_shell.return_value = subprocess.run('blabla1234', shell=True)
        if platform.system() == 'Windows':
            self.assertTrue(True)

        runner = CliRunner()
        with runner.isolated_filesystem():
            mock_env.return_value = 'test_user'
            info = find_project_data()
            assert info.get('author') == 'test_user'

    @unittest.mock.patch('manati.utils.click.secho')
    def test_task(self, mock_secho):

        @task('Before', 'After')
        def func():
            raise Exception

        with self.assertRaises(Exception):
            func()
            mock_secho.assert_called_with('ERROR')
