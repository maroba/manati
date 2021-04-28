import pathlib
import os
import shutil

import click

from manati.add import add_package, add_license, add_github_action
from manati.create import create_project, create_docs
from manati.utils import confirm_copy, find_project_data
import manati.utils as utils
from manati.validators import validate_project_name
from manati.deploy import deploy_pypi, deploy_github
from manati.run import run_tests, run_coverage, run_docs, run_flake8


@click.group('manati')
def cli():
    """\b
███╗   ███╗ █████╗ ███╗   ██╗ █████╗ ████████╗██╗
████╗ ████║██╔══██╗████╗  ██║██╔══██╗╚══██╔══╝██║
██╔████╔██║███████║██╔██╗ ██║███████║   ██║   ██║
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║   ██║   ██║
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║   ██║   ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝

    A command line interface (CLI) for managing Python projects.

"""
    pass


@cli.command('create')
@click.option('-n', '--name', 'name', required=True, callback=validate_project_name,
              prompt='Project name', help='Name of the project, same as the main package.')
@click.option('-G', '--no-git', 'no_git', is_flag=True, default=False,
              help='Do not create git repository')
@click.option('-I', '--no-install', 'no_install', is_flag=True, default=False,
              help='Do not pip-install in editable mode')
@click.option('-a', '--author', 'author', default=lambda: os.environ.get('USER', 'AUTHOR'), prompt='Author')
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


@cli.group('deploy')
def deploy(*args, **kwargs):
    """Deploy your project."""
    pass


@deploy.command('pypi')
def deploy_pypi_command():
    """Deploy project to PyPi package repository.

Remember to adjust the version, email and url in setup.py before submitting.
"""
    deploy_pypi()


@deploy.command('repo')
@click.option('-u', '--url', 'url', required=True, prompt='URL of the remote repository (github, gitlab, etc.)?',
              help='URL of the remote repository (github, gitlab, etc.)')
@click.option('-m', '--main-branch', 'main', required=True, default='main',
              prompt='Default branch (main, master, etc.)?',
              help='The default remote branch')
def deploy_repo_command(url, main):
    """Deploy local git repository to github, gitlab, bitbucket, etc."""
    deploy_github(url, main)


@cli.group('run')
def run(*args, **kwargs):
    """Run tests or analyze test coverage"""
    pass


@run.command('tests')
@click.option('-t', 'directory', required=True, prompt='Test folder', help='Directory with tests.')
@click.option('-r', '--runner', 'runner', required=True, default='unittest',
              type=click.Choice(['unittest', 'pytest'], case_sensitive=False),
              help='Test runner', prompt='Test runner')
def run_tests_command(directory, runner):
    """Run tests in a test folder."""
    run_tests(directory, runner)


@run.command('coverage')
@click.option('-s', '--source', 'source', required=True, help='Package on which to run coverage.',
              prompt='Source package',
              default=lambda: find_project_data().get('package', None))
@click.option('-t', '--tests', 'test_dir', required=True,
              prompt='Test folder', help='Directory with tests.',
              default=lambda: find_project_data().get('tests', None))
@click.option('-r', '--runner', 'runner', required=True, default='unittest',
              type=click.Choice(['unittest', 'pytest'], case_sensitive=False),
              help='Test runner', prompt='Test runner')
def run_coverage_command(source, test_dir, runner):
    """Run test coverage."""
    run_coverage(source, test_dir, runner)


@run.command('docs')
def run_docs_command():
    """Build the documentation and show it in browser."""
    run_docs()


@run.command('flake8')
@click.argument('dirs', nargs=-1)
def run_flake8_command(dirs):
    """Run PEP8 style enforcement.

But in contrast to PEP8, by default 120 characters per line are ok.
"""
    run_flake8(dirs)


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


@add.command('github-action')
@click.option('-p', '--package', 'package', required=True, prompt='Package',
              default=lambda: find_project_data().get('package', None))
@click.option('-t', '--tests', 'tests', required=True, prompt='Test folder',
              default=lambda: find_project_data().get('tests', None))
def add_github_action_command(package, tests):
    """Add github default action"""
    add_github_action(package, tests)


@cli.command('info')
def info_command():
    """Scan for project data."""

    info = find_project_data()
    info['python'] = utils.find_python()
    info['sphinx-quickstart'] = utils.find_sphinx_quickstart()
    info['sphinx-build'] = utils.find_sphinx_build()

    def echo_warning(title, key):
        value = info.get(key, 'NOT FOUND')
        if value == 'NOT FOUND':
            click.echo(title + value, nl=False)
            click.secho(' [!]', fg='red')
        else:
            click.echo(title + value)

    echo_warning('Project name: ', 'name')
    echo_warning('Package: ', 'package')
    echo_warning('Test directory: ', 'tests')
    echo_warning('Version: ', 'version')
    echo_warning('Author: ', 'author')
    echo_warning('Email: ', 'email')
    echo_warning('URL: ', 'url')
    echo_warning('Python: ', 'python')
    echo_warning('sphinx-quickstart: ', 'sphinx-quickstart')
    echo_warning('sphinx-build: ', 'sphinx-build')


if __name__ == '__main__':
    cli()
