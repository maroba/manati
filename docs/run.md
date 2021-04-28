# Running stuff

Depending on what helper tools you are using, you have to use 
different syntax, which is kind of annoying. For instance, I regularly
forget the proper way how to trigger the test discovery with the
*unittest* framework of the Python standard library. With *manati*
you have the choice to use different tools, but don't have to remember
the exact syntax for each of them.

Here is what you can currently run with *manati*:

```text
  coverage  Run test coverage.
  docs      Build the documentation and show it in browser.
  flake8    Run PEP8 style enforcement.
  tests     Run tests in a test folder.
```

## Run tests

To run your test suite with *manati*, type

```
manati run tests
```

You will be asked what testing framework you want to run your tests with.
Currently, *manati* supports *unittest* and *pytest* as two of the most
popular solutions. If you are missing your favorite framework, please submit
an issue with a feature request.

```text
Options:
  -t TEXT                         Directory with tests.  [required]
  -r, --runner [unittest|pytest]  Test runner  [required]
  --help                          Show this message and exit.
```

## Analyze test coverage

You can analyze the test coverage with *manati* by typing

```
manati run coverage
```

You will be asked which package to analyze and in which folder the
tests are located. If the defaults that *manati* is guessing are correct,
just confirm them with ENTER.

```text
Options:
  -s, --source TEXT               Package on which to run coverage.
                                  [required]

  -t, --tests TEXT                Directory with tests.  [required]
  -r, --runner [unittest|pytest]  Test runner  [required]
  --help                          Show this message and exit.
```

## Run docs

If your project has a `./docs` folder with a proper Sphinx documentation,
you can build the HTML files and show them in the browser by simply typing

```
manati run docs
```

## Run style enforcement

Proper code style is important, so you should follow the style recommendations
as defined in PEP8. However, the line length limitation of 79 characters is
extremely annoying. That is why *manati* uses 120 character per line as the
default in *flake8*. To scan for style deviations, run

```
Usage: manati run flake8 [DIRS]...

  Run PEP8 style enforcement.

  But in contrast to PEP8, by default 120 characters per line are ok.
```
