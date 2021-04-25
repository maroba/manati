import unittest
from os.path import exists

from click.testing import CliRunner

from manati.add import add_package


class TestAdd(unittest.TestCase):

    def test_add_package(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            add_package('level1.level2.level3')
            self.assertTrue(exists('level1/level2/level3/__init__.py'))


if __name__ == '__main__':
    unittest.main()
