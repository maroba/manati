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
@click.option('-n', '--name', 'name', required=True, callback=validate_project_name, prompt='Project name')
#@click.option('--no-git', is_flag=True, default=False)
#@click.option('--no-docs', is_flag=True, default=False)
def create_project_command(name):
    try:
        #click.echo(name)
        create_project(name)
    except Exception as e:
        click.echo(e)


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