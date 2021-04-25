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

Call `manati add --help` for more information.


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

