import pathlib
import os


def add_package(name):

    components = name.split('.')

    path = pathlib.Path('.')

    for comp in components:
        path = path / comp
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(path / '__init__.py'):
            with open(path / '__init__.py', 'w') as f:
                f.write('')
