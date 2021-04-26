from os.path import exists
from pathlib import Path
import shutil

import click

from manati.utils import shell


def deploy_pypi():

    cwd = Path.cwd()

    if not exists(cwd / 'setup.py'):
        raise click.UsageError('No setup.py found. Is this really a project root?')

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


def do_twine():
    click.echo('Log in to PyPi...')
    shell('twine upload *', 'dist', silent=False)
