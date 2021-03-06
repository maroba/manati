import pathlib
import os
import shutil

import click

from manati.utils import task, substitute, render


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
    """Adds a LICENSE file to specified directory.

    Parameters
    ----------
    path: str or pathlib.Path
        The directory where to put the LICENSE file.

    license: str [MIT|GPLv3|Apache]
        The type of license.
    """
    if isinstance(path, str):
        if path == '.' or path == './':
            path = pathlib.Path.cwd()
        else:
            path = pathlib.Path(path)

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
    substitute(setup_py, {"license='None'": "license='%s'" % license})


def add_github_action(package, tests):
    cwd = pathlib.Path.cwd()

    target = cwd / '.github' / 'workflows' / 'check.yml'
    if os.path.exists(target):
        if not click.confirm('check.yml already exists. Overwrite?'):
            click.Abort()
            return

    templates = pathlib.Path(__file__).parent / 'templates'
    if not os.path.exists(cwd / '.github'):
        os.mkdir(cwd / '.github')
    if not os.path.exists(cwd / '.github' / 'workflows'):
        os.mkdir(cwd / '.github' / 'workflows')

    render(target, templates / 'check.yml',
           {':PACKAGE:': package,
            ':TEST:': tests})
    click.echo('Created github action under ' + str(target))
