import unittest

from click.testing import CliRunner

from manati.manati import cli


class TestApropos(unittest.TestCase):

    def test_apropos_tests(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['apropos', 'tests'])
        assert result.exit_code == 0
        assert 'How to run tests' in result.output

    def test_apropos_install(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['apropos', 'install'])
        assert result.exit_code == 0
        assert 'How to install project for development' in result.output