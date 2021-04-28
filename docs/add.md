# Adding Stuff

If you already have a project, but it is missing some important
aspects like proper `setup.py`, license file, `.gitignore` or other,
you can add that easily with *manati*.

This is what you can add with *manati* in the current version:

```text
> manati add --help

Usage: manati add [OPTIONS] COMMAND [ARGS]...

  Adds something to the current project.

Options:
  --help  Show this message and exit.

Commands:
  docs           Add a docs folder with Sphinx documentation to the current...
  github-action  Add github default action
  gitignore      Add a default .gitignore file to the current directory.
  license        Add a license to the current project.
  package        Add a package to the current directory.
  setup.py       Add a setup.py file to the current directory
```

## Adding documentation

Documentation for Python projects (not docstrings) in usually stored in
the `./docs` folder under the project root directory. The quasi standard
for generating documentation in Python is [Sphinx](https://www.sphinx-doc.org).
If your project is missing a documentation, you can set it up with

```
manati add docs
```

and the folder and an initial documentation is set up. You can modify
the documentation settings and plugins used by editing the
`./docs/conf.py` file, which is the central configuration file for
Sphinx.

Now the initial documentation is ready to be generated, which can be done
by typing

```
manati run docs
```

from the project root directory. After the building process, a browser
opens up showing the resulting HTML files, which should look very similar
to the documentation you are currently reading.

## Adding *.gitignore* file

It is important not to clutter your *git* repository with files that are
not needed for the code itself. If your project does not yet have a suitable
`.gitignore` file that catches must of the irrelevant stuff, you can add one
to your project by typing

```
manati add gitignore
```

## Adding *setup.py* file

When you want to install your project to your Python environment so that
it can be used from anywhere in your file system, you need to have a
`setup.py` file for proper installation. You can add such a file to
your project by simply typing

```
manati add setup.py
``` 

After that, you may want to edit some of the settings in the file, 
like author, email, name of the package, etc.


## Adding a license

Defining a license for your project is important if you want other people
to use your code and control how they may use it. If your project is missing
a suitable license file, you can add one by

```
manati add license
```

You have the choice between several different typical license types. If you
are unsure which one to select, take a look at [choosealicense.com](https://choosealicense.com).

## Adding a package

Suppose you have a package `mypackage`. If you want to create a subpackage `foo`, and inside this one
another subsubpackage `bar`, you can do this in one step with *manati*:

```
manati add package mypackage.foo.bar
``` 

The proper `__init__.py` files are also created of course.

## Adding github-actions

When you want to host your *git* repository on [github.com](https://github.com), you may
want to use their continuous integration / continuos deployment tools, Github Actions.
To use that, your repository needs a hidden directory `./.github/worksflows/` containing
configuration files that define what actions to perform. With *manati* you can quickly
set that up for your project by simply typing

```
manati add github-action
```

You will be asked about the name of the package and the folder with the tests,
so that the tests can be run properly. You may not see the folder immediately,
because it is hidden, but it is there. :-) 

After you commit and push your repository to github, the action will be triggered. And 
it will also be triggered on every future push. 