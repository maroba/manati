import click
from manati.create import create_project


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


if __name__ == '__main__':
    cli()