import os
import pathlib
import datetime
import subprocess

import click


def create_project(name, no_git, no_install, author):
    path = pathlib.Path.cwd() / name
    if os.path.exists(path):
        raise Exception('ERROR: Path already exists.')

    templates = pathlib.Path(__file__).parent / 'templates'

    click.echo('Create project structure...', nl=False)
    os.makedirs(path)
    os.makedirs(path / name)

    subs = {
        'PROJECT_NAME': name,
        'YEAR': datetime.date.today().year,
        'VERSION': '0.0.1',
        'MODULE_NAME': 'main',
        'AUTHOR': author
    }
    render(path / 'setup.py', templates / 'setup.py', subs)
    render(path / name / 'main.py', templates / 'source.py', subs)
    render(path / name / '__init__.py')

    os.makedirs(path / 'tests')
    render(path / 'tests' / 'test_main.py', templates / 'test.py', subs)

    render(path / '.gitignore', templates / '.gitignore')

    click.echo('Done.')

    create_docs(path, name, author)

    if not no_git:
        click.echo('Create local git repository...', nl=False)
        shell('git init', root=name)
        click.echo('Done.')

    if not no_install:
        click.echo('Pip-installing as editable version...', nl=False)
        shell('pip install -e .', root=name)
        click.echo('Done.')

    click.echo('Happy coding!')


def create_docs(path, name, author):
    click.echo('Creating project documentation...', nl=False)

    os.makedirs(path / 'docs')
    render(path / 'docs' / 'requirements.txt', 'sphinx\nsphinx_rtd_theme\n')

    shell('pip install -r requirements.txt', root=name+'/docs')

    cmd = 'sphinx-quickstart -p %s -a "%s" -v 0.0.1 --no-sep -l en -r 0.0.1 docs' % (name,
                                                                    author,
                                                                    )
    shell(cmd, name)

    replace(path / 'docs' / 'conf.py', {'alabaster': 'sphinx_rtd_theme'})
    click.echo('Done')

    click.echo('Build documentation...', nl=False)

    shell('make html', root=name + '/docs')
    click.echo('OK')


def render(path, template=None, subs=None):

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


def replace(file, subs):
    with open(file, 'r') as f:
        content = f.read()

    if content:
        for key, value in subs.items():
            content = content.replace(key, value)
        with open(file, 'w') as f:
            f.write(content)


def shell(cmd, root=None):
    if root:
        cmd = 'cd ' + root + '; ' + cmd
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL)


if __name__ == '__main__':
    create_project('tee', False, False)
