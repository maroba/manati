import os
import pathlib

from manati.templates import SETUP_PY_TEMPLATE, SOURCE_TEMPLATE, TEST_TEMPLATE, GITIGNORE_TEMPLATE


def create_project(name, no_git, no_install):
    path = pathlib.Path.cwd() / name
    if os.path.exists(path):
        raise Exception('ERROR: Path already exists.')

    os.makedirs(path)
    os.makedirs(path / name)
    os.makedirs(path / 'tests')
    # os.makedirs(path / 'docs') # TODO: Autocreate documentation

    write_file(path / 'setup.py', SETUP_PY_TEMPLATE.replace('PROJECT_NAME', name))

    source = SOURCE_TEMPLATE.replace('PROJECT_NAME', name)
    write_file(path / name / 'main.py', source)
    write_file(path / name / '__init__.py', '')

    test = TEST_TEMPLATE.replace('PROJECT_NAME', name).replace('MODULE_NAME', 'main')
    write_file(path / 'tests' / 'test_main.py', test)

    write_file(path / '.gitignore', GITIGNORE_TEMPLATE)

    if not no_git:
        os.system('cd %s; git init' % name)

    if not no_install:
        os.system('cd %s; pip install -e .' % name)


def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)
