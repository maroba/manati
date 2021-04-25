import click


def validate_project_name(ctx, param, value):
    if ' ' in value:
        raise click.BadParameter('Whitespace in project name not allowed.')
    return value