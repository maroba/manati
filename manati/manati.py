import pathlib

import click

from manati.create import create_project
from manati.add import add_package, add_license
from manati.apropos import help_tests, help_install
from manati.validators import validate_project_name


@click.group('manati')
def cli(*args, **kwargs):
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


@cli.group('apropos')
def apropos(*args, **kwargs):
    """Print reminders on various topics."""
    pass


@apropos.command('tests')
def apropos_tests_command():
    """Help on how to run tests."""
    help_tests()


@apropos.command('install')
def apropos_install_command():
    """Help on how to install in development mode."""
    help_install()


if __name__ == '__main__':
    cli()