#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import exists
from setuptools import setup, find_packages

author = 'AUTHOR'
email = 'EMAIL'
description = 'DESCRIPTION'
name = 'PROJECT_NAME'
year = 'YEAR'
url = 'URL'
version = 'VERSION'

setup(
    name=name,
    author=author,
    author_email=email,
    url=url,
    version=version,
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,    
    license='None',
    description=description,
    long_description=open('README.md').read() if exists('README.md') else '',
    install_requires=['sphinx',
                      ],    
    python_requires=">=3.6",    
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 ],
    platforms=['ALL'],
)
