from os.path import exists
from pathlib import Path
import shutil

import click

from manati.utils import shell


def deploy_pypi():
    """Deploy project in current directory to PyPi."""

    cwd = Path.cwd()

    if not exists(cwd / 'setup.py'):
        raise click.UsageError(
            'No setup.py found. Is this really a project root?')

    if exists(cwd / 'build') or exists(cwd / 'dist'):
        if click.confirm('build and/or dist folder found which will be deleted. Continue?'):
            shutil.rmtree(cwd / 'build')
            shutil.rmtree(cwd / 'dist')
        else:
            click.Abort()
            return

    shell('pip install --upgrade wheel twine', silent=False)
    shell('python setup.py sdist bdist_wheel', silent=False)

    do_twine()


def deploy_github(url, main):
    shell('git remote add origin ' + url, silent=False)
    shell('git branch -M ' + main, silent=False)
    shell('git push -u origin ' + main, silent=False)


def do_twine():
    """Login and upload to PyPi."""
    click.echo('Log in to PyPi...')
    shell('twine upload *', 'dist', silent=False)
