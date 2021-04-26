import pathlib
import shutil
import os
from os.path import basename

import click

from manati.create import create_project, create_docs
from manati.add import add_package, add_license
from manati.validators import validate_project_name


@click.group('manati')
def cli():
    """Manati - a command line interface (CLI) for managing Python projects."""
    pass


@cli.command('create')
@click.option('-n', '--name', 'name', required=True, callback=validate_project_name,
              prompt='Project name', help='Name of the project, same as the main package.')
@click.option('-G', '--no-git', 'no_git', is_flag=True, default=False,
              help='Do not create git repository')
@click.option('-I', '--no-install', 'no_install', is_flag=True, default=False,
              help='Do not pip-install in editable mode')
@click.option('-a', '--author', 'author', default='AUTHOR', prompt='Author')
@click.option('-d', '--description', 'description', default='', prompt='(Short) description')
@click.option('-l', '--license', 'license', type=click.Choice([
    'MIT', 'GPLv3', 'Apache', 'None'
], case_sensitive=False), prompt='License', default='None')
def create_project_command(name, no_git, no_install, author, description, license):
    """Create a standard Python project structure.

    By default, the project is also pip-installed for development
    in editable mode, and a local git repository is also created.
    """
    try:
        create_project(name, no_git, no_install, author, description, license)
    except Exception as e:
        click.echo(e)


@cli.group('add')
def add(*args, **kwargs):
    """Adds something to the current project."""
    pass


@add.command('docs')
def add_docs_command():
    """Add a docs folder with Sphinx documentation to the current directory."""
    cwd = pathlib.Path.cwd()
    create_docs(cwd, 'PROJECT_NAME', 'AUTHOR')


@add.command('package')
@click.argument('package_name')
def add_package_command(package_name):
    """Add a package to the current directory.

    PACKAGE_NAME must be the fully qualified package name, e.g.

         manati add package myproject.mypackage
    """
    click.echo('Create package...', nl=False)
    add_package(package_name)
    click.echo('Done.')


@add.command('license')
@click.option('-n', '--name', 'name', type=click.Choice(['MIT', 'GPLv3', 'Apache', 'None'], case_sensitive=False),
              required=True, prompt='License')
def add_license_command(name):
    """Add a license to the current project."""
    add_license(pathlib.Path.cwd(), name)


@add.command('gitignore')
def add_gitignore_command():
    """Add a default .gitignore file to the current directory."""
    cwd = pathlib.Path.cwd()
    target = cwd / '.gitignore'
    source = pathlib.Path(__file__).parent / 'templates' / '.gitignore'

    confirm_copy(source, target)


@add.command('setup.py')
def add_setup_py_command():
    """Add a setup.py file to the current directory"""
    cwd = pathlib.Path.cwd()
    target = cwd / 'setup.py'
    source = pathlib.Path(__file__).parent / 'templates' / 'setup.py'

    confirm_copy(source, target)


def confirm_copy(source, target):
    if not os.path.exists(target):
        shutil.copyfile(source, target)
    else:
        if click.confirm('%s file already exists in current directory. Overwrite?' % basename(target)):
            shutil.copyfile(source, target)


@cli.group('apropos')
def apropos(*args, **kwargs):
    """Print reminders on various topics."""
    pass


@apropos.command('tests')
def apropos_tests_command():
    """
How to run tests
****************

   python -m unittest discover tests
"""
    click.echo(apropos_tests_command.__doc__)


@apropos.command('install')
def apropos_install_command():
    """How to install project for development
**************************************

In order to install your own project for development, install it in
development mode (a.k.a editable mode). From the project root directory,
submit:

    pip install -e .

or

    python setup.py develop
"""
    click.echo(apropos_install_command.__doc__)


if __name__ == '__main__':
    cli()
