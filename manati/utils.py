import functools
import os
import re
import shutil
import subprocess
from pathlib import Path
from os.path import basename, exists

import click

class NotFoundException(Exception):
    pass


def task(msg_before, msg_after=None):
    def outer_wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):
            click.echo(msg_before, nl=not msg_after)
            try:
                result = func(*args, **kwargs)
                if msg_after:
                    click.secho(msg_after, fg='green')
                return result
            except Exception as e:
                click.secho('ERROR', fg='red')
                raise e
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


def shell(cmd, root=None, silent=True):
    """ Silently perform a shell command.

    Parameters
    ----------
    cmd: str
        The command to perform.

    root: path or str
        The directory where to perform the command. Default: current directory.
    """
    if root:
        cmd = 'cd ' + root + '&& ' + cmd
    if silent:
        return subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL)
    return subprocess.run(cmd, shell=True)


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


def confirm_copy(source, target):
    if not os.path.exists(target):
        shutil.copyfile(source, target)
    else:
        if click.confirm('%s file already exists in current directory. Overwrite?' % basename(target)):
            shutil.copyfile(source, target)


def file_content(path):
    if not os.path.exists(path):
        return ''

    with open(path, 'r') as f:
        content = f.read()
    return content


def find_project_data():
    """Try to find relevant project data.

    Should be executed from the project root directory (the one with the setup.py).
    """
    cwd = Path.cwd()

    # parse setup.py

    def find_parameter(par_name, text):

        pattern = re.compile(par_name + r'\s*=\s*([^,)}\n]+)')
        matches = pattern.findall(text)
        parameter = None
        for m in matches:
            result = re.search("'([^']*)'", m)
            if result:
                parameter = result.group(1)
            result = re.search('"([^"]*)"', m)
            if result:
                parameter = result.group(1)
            if parameter is not None:
                break
        return parameter

    setup_py = file_content(cwd / 'setup.py')

    info = dict()
    for key in ['name', 'url', 'version', 'email', 'author']:
        value = find_parameter(key, setup_py)
        if value is not None:
            info[key] = value

    if info.get('name') and exists(cwd / info['name']):
        info['package'] = info['name']

    test_dir = cwd / 'tests'
    if exists(test_dir) and os.path.isdir(test_dir):
        info['tests'] = 'tests'

    if 'tests' not in info:
        test_dir = cwd / 'test'
        if exists(test_dir) and os.path.isdir(test_dir):
            info['tests'] = 'test'

    return info


def find_python():
    found = shutil.which('python')
    if not found:
        found = shutil.which('py')
    return found


def find_sphinx_quickstart():
    return shutil.which('sphinx-quickstart')


def find_sphinx_build():
    return shutil.which('sphinx-build')
