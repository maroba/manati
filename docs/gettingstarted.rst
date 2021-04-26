Getting Started
===============

`manati` is a Python command line interface (CLI) for managing
Python projects.

Installation
************

Use `pip` for installation of `manati`:

.. code-block::

    pip install --upgrade manati

Usage
*****

Getting Help
------------

For all commands in *manati* you can get help on the command line by
adding a *--help* option to the command, for instance:

.. code-block::

    manati --help

shows the usage and all available subcommand.


Creating a project
------------------

In order to create a Python project `myproject`, go to the directory where
you want the project to be located. Then submit

.. code-block::

    manati create

This will create a default directory structure for Python projects,
source and test templates, as well as a ready-to-go *setup.py*
and *.gitignore* file, documentation based on Sphinx, a license file,
README, etc.

Adding stuff to an existing project
-----------------------------------

Sometimes you have an existing project, but initially you did not choose a license,
or your `.gitignore` is missing. You can add those special files with the `manati add` command.

You can add

- a `setup.py` file
- a `.gitignore` file
- choose a license
- a package
- a `docs` folder with Sphinx documentation

Call `manati add --help` for more information.

Run tests and test coverage
---------------------------

Run your test suite with

.. code-block::

    manati run tests

where you have the choice of two different test runners.

Analyze the test coverage with

.. code-block::

    manati run coverage

This shows you the percentage of test coverage for each module and
the lines that are not covered.

Deploy to PyPi
--------------

You can deploy your project to PyPi using *manati*:

.. code-block::

    manati deploy

As a prerequisite for deployment, you need an account at *PyPi*. You can register for one
here register_.

.. _register: https://pypi.org/account/register/

Please remember that you have to insert valid values for `version`, `email` and `url` in the
`setup.py` file.
