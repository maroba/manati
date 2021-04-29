from os.path import exists
from pathlib import Path

import click

from manati.utils import shell, find_python


def run_tests(test_folder, runner):

    if not exists(test_folder):
        raise click.BadParameter('No such folder %s' % test_folder)

    if runner == 'unittest':
        shell(find_python() + ' -m unittest discover ' + str(test_folder), silent=False)
    elif runner == 'pytest':
        shell(find_python() + ' -m pip install --upgrade pytest')
        shell(find_python() + ' -m pytest ' + str(test_folder), silent=False)
    else:
        raise click.BadParameter('No such test runner: %s' % runner)


def run_coverage(source, test_dir, runner):

    if not exists(test_dir):
        raise click.BadParameter('No such folder or file: %s' % test_dir)

    if not exists(source):
        raise click.BadParameter('No such folder %s' % source)

    if runner == 'unittest':
        shell(find_python() + ' -m pip install --upgrade coverage')
        shell(find_python() + ' -m coverage run --source=%s -m unittest discover %s' %
              (source, test_dir), silent=False)
    elif runner == 'pytest':
        shell(find_python() + ' -m pip install --upgrade coverage pytest')
        shell(find_python() + ' -m coverage run --source=%s -m pytest %s' %
              (source, test_dir), silent=False)
    else:
        raise click.BadParameter('No such test runner: %s' % runner)

    shell(find_python() + ' -m coverage report -m', silent=False)


def run_docs():
    """Build the documentation and show it in the browser."""

    cwd = Path.cwd()
    if not exists(cwd / 'docs'):
        raise click.BadParameter('Cannot find docs folder.')

    shell('make clean', root=str(cwd / 'docs'), silent=False)
    shell(find_python() + ' -m sphinx.cmd.build -M html . _build', root=str(cwd / 'docs'), silent=False)
    click.launch(str(cwd / 'docs' / '_build' / 'html' / 'index.html'))


def run_flake8(dirs):
    """Run flake8 style enforcement in specified directories.

    Parameters
    ----------
    dirs: list of str
        The directories to scan for style violations.
    """

    shell(find_python() + ' -m pip install --upgrade flake8')
    shell(find_python() + ' -m flake8 ' + ' '.join(dirs) + ' --max-line-length=120', silent=False)
