
# manati

A command line interface (CLI) for managing Python projects.

![https://de.vecteezy.com/gratis-vektor/natur](docs/images/manati.png) 

[![PyPI version](https://badge.fury.io/py/manati.svg)](https://badge.fury.io/py/manati)
![Build status](https://img.shields.io/github/workflow/status/maroba/manati/Checks)
![Coverage](https://img.shields.io/codecov/c/github/maroba/manati/main.svg)
[![Doc Status](https://readthedocs.org/projects/manati/badge/?version=latest)](https://manati.readthedocs.io/en/latest/index.html)

Create new Python projects with ready-to-go recommended project structure. 

Add important files to existing projects
like `setup.py`, `.gitignore`, Sphinx documentation, choose a license and more.


## Usage

### Creating a project

```
manati create -n myproject
```

creates a complete Python project structure inside the current working directory:

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

including sample source,
tests, documentation, `setup.py`, local `git` repository and a
suitable `.gitignore` file.

After creation, the project is already installed in development (editable) mode, so you can start coding right away.


### Adding stuff to an existing project

Sometimes you have an existing project, but initially you did not choose a license,
or your `.gitignore` is missing. You can add those special files with the `manati add` command.

You can add

- `setup.py` file
- `.gitignore` file
- choose a license
- new packages
- `docs` folder with Sphinx documentation

Call `manati add --help` for more information.

## Installation

Just use `pip`:

```
pip install --upgrade manati
```

## Documentation

The full documentation can be found [here](https://manati.readthedocs.io/en/latest/).


## Requirements

All Python requirements are installed automatically. However, **you need to have `git` installed**.

## Contributing

Suggestions for improvement or correction are always welcome, just submit an issue. If you want to contribute writing code or
documentation, please work on the `dev` branch and send a pull request.

#### Credits

Images by [Natur Vektoren von Vecteezy](https://de.vecteezy.com/gratis-vektor/natur).
