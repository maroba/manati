import functools
import os
import re
import subprocess

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


def substitute(path, pattern, replacement):
    with open(path, 'r') as f:
        content = f.read()

    content = re.sub(pattern, replacement, content)

    with open(path, 'w') as f:
        f.write(content)


def replace(path, subs):
    with open(path, 'r') as f:
        content = f.read()

    if content:
        for key, value in subs.items():
            content = content.replace(key, value)
        with open(path, 'w') as f:
            f.write(content)


def shell(cmd, root=None):
    """ Silently perform a shell command.

    Parameters
    ----------
    cmd: str
        The command to perform.

    root: path or str
        The directory where to perform the command. Default: current directory.
    """
    if root:
        cmd = 'cd ' + root + '; ' + cmd
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL)


def render(path, template=None, subs=None):
    """ Write a file based on a file or string template.

    Parameters
    ----------
    path: str or Pathlib path
        The path of the file to write.

    template: Path or str
        The file path or the string used as template.

    subs: dict
        The substitutions to perform on the template.
    """
    if template:
        if os.path.exists(template):
            with open(template, 'r') as f:
                content = f.read()
        else:
            content = template
    else:
        content = ''

    if subs:
        for key, value in subs.items():
            content = content.replace(key, str(value))

    with open(path, 'w') as f:
        f.write(content)