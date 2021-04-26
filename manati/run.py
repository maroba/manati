from os.path import exists

import click

from manati.utils import shell


def run_tests(test_folder):

    if not exists(test_folder):
        click.BadParameter('No such folder %s' % test_folder)

    shell('python -m unittest discover ' + str(test_folder), silent=False)


def run_coverage(source, test_dir):

    if not exists(test_dir):
        click.BadParameter('No such folder %s' % test_dir)

    if not exists(source):
        click.BadParameter('No such folder %s' % source)

    shell('pip install --upgrade coverage')
    shell('coverage run --source=%s -m unittest discover %s' % (source, test_dir), silent=False)
    shell('coverage report -m', silent=False)
