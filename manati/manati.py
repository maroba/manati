import pathlib

import click

from manati.create import create_project, create_docs
from manati.add import add_package, add_license
from manati.utils import confirm_copy
from manati.validators import validate_project_name
from manati.deploy import deploy_pypi
from manati.run import run_tests, run_coverage


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


@cli.command('deploy')
@click.option('-i', '--index', 'package_index', type=click.Choice(['pypi'], case_sensitive=False),
            prompt='Package index', default='pypi')
def deploy(package_index):
    """Deploy project to package repository.

Remember to adjust the version, email and url in setup.py before submitting.
    """
    if package_index != 'pypi':
        raise click.BadParameter('No such index: %s' % package_index)

    deploy_pypi()


@cli.group('run')
def run(*args, **kwargs):
    pass


@run.command('tests')
@click.option('-d', 'directory', required=True, prompt='Test folder', help='Directory with tests.')
@click.option('-r', '--runner', 'runner', required=True, default='unittest',
              type=click.Choice(['unittest', 'pytest'], case_sensitive=False),
              help='Test runner', prompt='Test runner')
def run_tests_command(directory, runner):
    """Run tests in a test folder."""
    run_tests(directory, runner)


@run.command('coverage')
@click.option('-s', '--source', 'source', required=True, help='Package on which to run coverage.',
              prompt='Source package')
@click.option('-t', '--tests', 'test_dir', required=True, prompt='Test folder', help='Directory with tests.')
@click.option('-r', '--runner', 'runner', required=True, default='unittest',
              type=click.Choice(['unittest', 'pytest'], case_sensitive=False),
              help='Test runner', prompt='Test runner')
def run_coverage_command(source, test_dir, runner):
    """Run test coverage."""
    run_coverage(source, test_dir, runner)


if __name__ == '__main__':
    cli()
