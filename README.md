
# manati

A command line interface (CLI) for managing Python projects.

![https://de.vecteezy.com/gratis-vektor/natur](docs/images/manati.png) 

[![PyPI version](https://badge.fury.io/py/manati.svg)](https://badge.fury.io/py/manati)
![Build status](https://img.shields.io/github/workflow/status/maroba/manati/Checks)
[![Doc Status](https://readthedocs.org/projects/manati/badge/?version=latest)](https://manati.readthedocs.io/en/latest/index.html)




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

#### Running tests

A smoke test as template for further tests is also created and you can run the tests as usual like so:

```
python -m unittest discover tests
```

#### Building the project documentation

After creation of the project, a documentation folder using Sphinx has been prepared, and the first version has
already been built. You can look at the documentation using your favorite brower by opening `myproject/docs/_build/html/index.html`.

If you want to update the documentation, rebuild by

```
cd docs
make clean
make html
```

### Adding stuff to an existing project

Sometimes you have an existing project, but initially you did not choose a license,
or your `.gitignore` is missing. You can add those special files with the `manati add` command.

You can add

- a `setup.py` file
- a `.gitignore` file
- choose a license
- a package
- a `docs` folder with Sphinx documentation

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

#### Credits

Images by [Natur Vektoren von Vecteezy](https://de.vecteezy.com/gratis-vektor/natur).
