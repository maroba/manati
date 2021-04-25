import click
from manati.create import create_project
from manati.apropos import help_tests, help_install


def validate_project_name(ctx, param, value):
    if ' ' in value:
        raise click.BadParameter('Whitespace in project name not allowed.')
    return value


@click.group('manati')
def cli(*args, **kwargs):
    pass


@cli.group('create')
def create(*args, **kwargs):
    pass


@create.command('project')
@click.option('-n', '--name', 'name', required=True, callback=validate_project_name,
              prompt='Project name', help='Name of the project, same as the main package.')
@click.option('-G', '--no-git', 'no_git', is_flag=True, default=False,
              help='Do not create git repository')
@click.option('-I', '--no-install', 'no_install', is_flag=True, default=False,
              help='Do not pip-install in editable mode')
@click.option('-a', '--author', 'author', default='AUTHOR', prompt='Author')
@click.option('-d', '--description', 'description', default='', prompt='(Short) description')
def create_project_command(name, no_git, no_install, author, description):
    """Create a standard Python project structure.

    By default, the project is also pip-installed for development
    in editable mode, and a local git repository is also created.
    """
    try:
        create_project(name, no_git, no_install, author, description)
    except Exception as e:
        click.echo(e)


@cli.group('apropos')
def apropos(*args, **kwargs):
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