import pathlib
import os
import shutil
import re

import click

from manati.utils import task

@task('Create package...', ' OK')
def add_package(name):
    """ Add a package structure in the current working directory

    Parameters
    ----------
    name: str
        Name of the package including parent packages.
    """
    components = name.split('.')

    path = pathlib.Path('.')

    for comp in components:
        path = path / comp
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(path / '__init__.py'):
            with open(path / '__init__.py', 'w') as f:
                f.write('')


def add_license(path, license):

    if os.path.exists(path / 'LICENSE'):
        raise click.BadParameter('LICENSE file already existing.')

    templates_dir = pathlib.Path(__file__).parent / 'templates' / 'licenses'

    files = {'MIT': templates_dir / 'MIT',
             'GPLv3': templates_dir / 'GPLv3',
             'Apache': templates_dir / 'Apache'
             }

    shutil.copyfile(files[license], path / 'LICENSE')

    setup_py = path / 'setup.py'
    if not os.path.exists(setup_py):
        click.echo('Warning: cannot find setup.py to set license type.')
        return
    substitute(setup_py, "license='None'", "license='%s'" % license)


def substitute(path, pattern, replacement):
    with open(path, 'r') as f:
        content = f.read()

    content = re.sub(pattern, replacement, content)

    with open(path, 'w') as f:
        f.write(content)