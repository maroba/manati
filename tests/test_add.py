import unittest
from os.path import exists, getsize
from pathlib import Path


from click.testing import CliRunner

from manati.add import add_package, add_license
from manati.utils import shell
from manati.manati import cli


class TestAdd(unittest.TestCase):

    def test_add_package(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            add_package('level1.level2.level3')
            self.assertTrue(exists('level1/level2/level3/__init__.py'))

    def test_add_license(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            shell('touch setup.py')
            cwd = Path.cwd()
            add_license(cwd, 'MIT')
            self.assertTrue(exists(cwd / 'LICENSE'))

    def test_add_license_with_string(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            shell('touch setup.py')
            add_license('.', 'MIT')
            self.assertTrue(exists(Path.cwd() / 'LICENSE'))

    def test_add_gitignore(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            runner.invoke(cli, ['add', 'gitignore'])
            cwd = Path.cwd()
            self.assertTrue(exists(cwd / '.gitignore'))

    def test_add_setup_py(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            runner.invoke(cli, ['add', 'setup.py'])
            cwd = Path.cwd()
            self.assertTrue(exists(cwd / 'setup.py'))

    def test_add_setup_py_overwrite(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            shell('touch setup.py')
            cwd = Path.cwd()
            assert getsize(cwd / 'setup.py') == 0
            runner.invoke(cli, ['add', 'setup.py'], input='y\n')

            self.assertTrue(exists(cwd / 'setup.py'))
            assert getsize(cwd / 'setup.py') > 0


if __name__ == '__main__':
    unittest.main()
