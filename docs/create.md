# Creating a new project

*manati* can set up a default and ready-to-go structure for Python projects that contains
probably everything you need (if not, submit an issue at [github](https://github.com/maroba/manati) :-) ).

Suppose you want to create a project named *myproject*. Go to the directory where you want 
the new project to be created and type

```
manati create
```

You will be prompted for a few questions for setting up the project (defaults in square brackets can simply
be accepted by pressing ENTER):

```
Project name: myproject
Author [mbaer]: maroba
(Short) description []: My fancy new project
License (MIT, GPLv3, Apache, None) [None]: MIT
```

After that *manati* sets up the following directory structure:

```
myproject
├── docs
│   ├── Makefile
│   ├── conf.py
│   ├── index.rst
│   ├── make.bat
│   └── requirements.txt
├── myproject
│   ├── __init__.py
│   └── main.py
├── LICENSE
├── README.md
├── setup.py
├── .gitignore
└── tests
    └── test_main.py
```

The `./docs` folder contains documentation for the project in Read-The-Docs style based on
Python's quasi standard [Sphinx](https://www.sphinx-doc.org), and a first HTML version has
also been built. You can watch it by opening `./docs/_build/html/index.html` in your browser
or, more easily by running

```
manati run docs
``` 

which will (re-)build the docs and open it up in a browser.

The `.gitignore` file that has been created contains most of the file patterns
which should not be part of a *git* repository of Python projects.

A local *git* repository has also been created as you can see by typing

```
cd myprojects
git status
```

The newly created project also contains a `setup.py` in the project root
directory, that is used for installation in development mode and also for
later deployment to a package index like PyPi. You may want to adjust some
settings in the `setup.py` file, like your email address, the project URL
or maybe the intended audience classifiers. You can look up valid
classifiers at [PyPi](https://pypi.org/classifiers/). 

After creation, *manati* has already installed it in development mode,
so you can start coding and any changes will be automatically be taken
into account without the need to re-import anything.

A sample code module `myproject/main.py` has been created along with
a test module `tests/test_main.py`. You can run the test suite with
your favorite testing framework, for instance with the *unittest* framework
from Python's standard library:

```
python -m unittest discover tests
``` 

or alternatively with *manati*:

```
manati run tests
```

where you have the choice between different testing frameworks.



### All options

Creating a new project can also be done in one line by specifying the
required information as options:

```
> manati create --help

Usage: manati create [OPTIONS]

  Create a standard Python project structure.

  By default, the project is also pip-installed for development in editable
  mode, and a local git repository is also created.

Options:
  -n, --name TEXT                 Name of the project, same as the main
                                  package.  [required]

  -G, --no-git                    Do not create git repository
  -I, --no-install                Do not pip-install in editable mode
  -a, --author TEXT
  -d, --description TEXT
  -l, --license [MIT|GPLv3|Apache|None]
  --help                          Show this message and exit.
```