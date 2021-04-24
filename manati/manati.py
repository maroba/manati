import click
from manati.create import create_project
from manati.apropos import help_tests, help_install


@click.group('manati')
def cli(*args, **kwargs):
    pass


@cli.group('create')
def create(*args, **kwargs):
    pass


@create.command('project')
@click.argument('project_name')
def create_project_command(project_name):
    try:
        create_project(project_name)
    except Exception as e:
        print(e)


@cli.group('apropos')
def apropos(*args, **kwargs):
    pass


@apropos.command('tests')
def apropos_tests_command():
    help_tests()


@apropos.command('install')
def apropos_install_command():
    help_install()


if __name__ == '__main__':
    cli()