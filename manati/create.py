import os
import pathlib
import datetime


def create_project(name, no_git, no_install):
    path = pathlib.Path.cwd() / name
    if os.path.exists(path):
        raise Exception('ERROR: Path already exists.')

    templates = pathlib.Path(__file__).parent / 'templates'

    os.makedirs(path)
    os.makedirs(path / name)
    os.makedirs(path / 'tests')

    subs = {
        'PROJECT_NAME': name,
        'YEAR': datetime.date.today().year,
        'VERSION': '0.0.1',
        'MODULE_NAME': 'main'
    }
    render(path / 'setup.py', templates / 'setup.py', subs)
    render(path / name / 'main.py', templates / 'source.py', subs)
    render(path / 'tests' / 'test_main.py', templates / 'test.py', subs)
    render(path / name / '__init__.py')
    render(path / name / '.gitignore', templates / '.gitignore')

    if not no_git:
        os.system('cd %s; git init' % name)

    if not no_install:
        os.system('cd %s; pip install -e .' % name)


def render(path, template=None, subs=None):

    if template:
        with open(template, 'r') as f:
            content = f.read()
    else:
        content = ''

    if subs:
        for key, value in subs.items():
            content = content.replace(key, str(value))

    with open(path, 'w') as f:
        f.write(content)
