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

Creating a project
------------------

In order to create a Python project ``myproject, go to the directory where
you want the project to be located. Then submit

.. code-block::

    manati create project myproject

This will create a default directory structure for Python projects,
source and test templates, as well as a ready-to-go *setup.py*
and *.gitignore* file, in case you want to work with a *git* repository.

Getting Help
------------

For all commands in *manati* you can get help on the command line by
adding a *--help* option to the command, for instance:

.. code-block::

    manati --help

shows the usage and all available subcommand.


Apropos
-------

I often forget how to do typical tasks on the command line, like
how to run all available tests in a directory. To get a reminder,
you can use the `manati apropos` command. For example,

.. code-block::

    manati apropos tests

shows::

    How to run tests
    ****************

       python -m unittest discover tests



All available *apropos* subcommands can be found by::

    manati apropos --help

