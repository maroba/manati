#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import exists
from setuptools import setup, find_packages

author = 'Matthias Baer'
email = 'matthias.r.baer@googlemail.com'
description = 'A CLI for managing Python projects.'
name = 'manati'
year = '2021'
version = '0.3.1'

setup(
    name=name,
    author=author,
    author_email=email,
    url='https://github.com/maroba/manati',
    version=version,
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,
    entry_points='''
        [console_scripts]
        manati=manati.manati:cli
    ''',
    license="GPL v3",
    description=description,
    long_description=open('README.md').read() if exists('README.md') else '',
    long_description_content_type="text/markdown",
    install_requires=['Click',
                      'sphinx'
                      ],
    # not to be confused with definitions in pyproject.toml [build-system]
    python_requires=">=3.6",
    keywords=['CLI', 'cli', 'Python project management'],
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 'Intended Audience :: Developers',
                 'Environment :: Console'
                 ],
    platforms=['ALL'],
)
