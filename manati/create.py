import os
import pathlib
import datetime
import subprocess

import click

from manati.utils import task
from manati.add import add_license


def create_project(name, no_git, no_install, author, description, license):
    """ Create a Python project structure in the current working directory.

    Parameters
    ----------
    name: str
        Name of the project. Also the main package name.

    no_git: bool
        If true, do not create local git repository.

    no_install: bool
        If true, do not pip-install in editable mode.

    author: str
        Author of the project.

    description:
        Short description of the project. Used for README and setup.py.
    """

    path = pathlib.Path.cwd() / name
    if os.path.exists(path):
        raise Exception('ERROR: Path already exists.')

    templates = pathlib.Path(__file__).parent / 'templates'
    subs = {
        'PROJECT_NAME': name,
        'YEAR': datetime.date.today().year,
        'VERSION': '0.0.1',
        'MODULE_NAME': 'main',
        'AUTHOR': author,
        'DESCRIPTION': description
    }

    create_project_structure(name, path, subs, templates)

    if license != 'None':
        add_license(path, license)

    create_docs(path, name, author)
    build_documentation(name)

    if not no_git:
        create_git_repo(name)

    if not no_install:
        pip_install_project(name)

    click.echo('Happy coding!')


@task('Create project structure...', ' OK')
def create_project_structure(name, path, subs, templates):
    os.makedirs(path)
    os.makedirs(path / name)
    render(path / 'README.md', templates / 'README.md', subs)
    render(path / 'setup.py', templates / 'setup.py', subs)
    render(path / name / 'main.py', templates / 'source.py', subs)
    render(path / name / '__init__.py')
    os.makedirs(path / 'tests')
    render(path / 'tests' / 'test_main.py', templates / 'test.py', subs)
    render(path / '.gitignore', templates / '.gitignore')


@task('Pip-installing as editable version...', 'OK')
def pip_install_project(name):
    shell('pip install -e .', root=name)


@task('Create local git repository...', ' OK')
def create_git_repo(name):
    shell('git init', root=name)


@task('Creating project documentation...', ' OK')
def create_docs(path, name, author):
    """ Create a project documentation.

    Parameters
    ----------
    path: str or Pathlib path
        Path of the project root. Folder 'docs' will be created as subfolder.

    name: str
        Name of the project

    author:
        Author of the project
    """

    os.makedirs(path / 'docs')
    render(path / 'docs' / 'requirements.txt', 'sphinx\nsphinx_rtd_theme\n')

    shell('pip install -r requirements.txt', root=name+'/docs')

    cmd = 'sphinx-quickstart -p %s -a "%s" -v 0.0.1 --no-sep -l en -r 0.0.1 docs' % (name,
                                                                    author,
                                                                    )
    shell(cmd, name)

    replace(path / 'docs' / 'conf.py', {'alabaster': 'sphinx_rtd_theme'})


@task('Build documentation...', ' OK')
def build_documentation(name):
    shell('make html', root=name + '/docs')


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

