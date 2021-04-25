import functools

import click


def task(msg_before, msg_after=None):
    def outer_wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):
            click.echo(msg_before, nl=not msg_after)
            func(*args, **kwargs)
            if msg_after:
               click.echo(msg_after)
        return inner_wrapper
    return outer_wrapper