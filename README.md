
# manati
A Python CLI for managing Python projects.
![abc](docs/images/manati.png) 

[![PyPI version](https://badge.fury.io/py/manati.svg)](https://badge.fury.io/py/manati)
[![Doc Status](https://readthedocs.org/projects/manati/badge/?version=latest)](https://manati.readthedocs.io/en/latest/index.html)




## Usage

### Creating a project

```
manati create project myproject
```

creates a complete Python project structure inside the current working directory:

```
myproject/
├── myproject
│   └── __init__.py
│   └── main.py
├── setup.py
└── tests
    └── test_main.py
```

including sample source,
tests, documentation, `setup.py`, local `git` repository and a
suitable `.gitignore` file.

## Installation

Just use `pip`:

```
pip install --upgrade manati
```

## Documentation

The full documentation can be found [here](https://manati.readthedocs.io/en/latest/).
