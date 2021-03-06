# How to contribute

*manati* is open source and everyone is welcome to contribute in its development! 

## Report bugs and feature requests 

If you are missing a feature or have found a bug, please
[submit an issue](https://github.com/maroba/manati/issues). There are no formal requirements
for how an issue should look like. If you have found a bug, please also give
input, output and error messages, if possible. Maybe you already know how to solve it. In
that case you could describe the solution, or alternatively, fix it yourself (see description below).

## Contributing code or documentation

Of course, you can clone the *manati* repository to your local machine and
change the code there, but then you cannot feed your changes back to the original
repository. When you want your changes to be part of *manati*, you should **fork**
the [*manati* repository](https://github.com/maroba/manati) instead. This creates
a copy of the repository in your own space on github.

### Set up development environment

Clone *your fork* of *manati* to your machine, go to the project root directory
of *manati* (where `setup.py` is located) and type

```
pip install -e .
``` 

This installs *manati* in editable / development mode. So any changes to the
code will automatically be active for any local users of the code. That's all.

### Developing code

Please be sure to write tests for all your changes. The tests are located
in `./tests` and there is one test module per code module. The naming convention
is `./tests/test_MODULENAME.py` if you have a module `./manati/MODULENAME.py`.
 
 *manati* uses
the *unittest* framework from the Python standard library. So please
stick with that. You can run the test suite from the project root
directory by

```
manati run tests
```

Remember, even *manati* can be managed using *manati*. :-)

We strive for a high test coverage, so please make sure that your changes
do not decrease the percentage of covered lines. You can run the coverage
by

```
manati run coverage
```

And needless to mention: Please do not commit failing tests!

When changing the code base, please follow typical PEP8 style conventions,
**except for the max. line length rule**. *manati* code should have a maximum 
line length of 120 characters. You can check for style violations by typing

```
manati run flake8
```

from the project root directory.

Once you are ready with your changes, covered by tests and **all** the tests
 are running, send a pull request from your fork:

![pull request](images/fork.png)


### Writing documentation

The documentation is in the `./docs` folder. The starting page `./docs/index.rst` is
in reStructuredText format, but all other pages are Markdown files. Please stick to
Markdown, if possible.

When you have made changes to the documentation, build it. This can be done with *manati*
itself from the project root directory:

```
manati run docs
```

Watch out for error messages in the console in case you have introduced some bugs to
the documentation. A browser opens up with the newly built pages. If satisfied, commit
your changes to your local git repository, push them to your remote repository,
and send a pull request.  


