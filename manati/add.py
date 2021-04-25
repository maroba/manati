import pathlib
import os

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
