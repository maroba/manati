# Deploy your project

When your code is ready to share with other
Python developers, you should submit your repository to a platform like 
github.com, so that people can contribute to your project. And when you want
people in the world to be *pip install* your package, you should submit your
code to the package index PyPi. Both things can be done with *manati*:

```text
Usage: manati deploy [OPTIONS] COMMAND [ARGS]...

  Deploy your project.

Options:
  --help  Show this message and exit.

Commands:
  pypi  Deploy project to PyPi package repository.
  repo  Deploy local git repository to github, gitlab, bitbucket, etc.
```

## Deploy to PyPi

From the root directory of your project (where the `setup.py` is located), type

```
manati deploy pypi
```

In the background, *manati* will install and update any requirements needed 
deployment and then build your code and create folders `dist` and `build`.
Then it will upload the package to PyPi, that's why you are asked to enter your
PyPi username and password. Of course, this means that you have to have a PyPi account
first, which you can [register here](https://pypi.org/account/register/).

If everything goes right, at the end *manati* prints a link to your submitted
package at [pypi.org](https://pypi.org). It is online now and can be installed with
*pip* by anyone in the world.

So what can go wrong? In the `setup.py` file (if you don't have one yet, 
[add it with *manati*](add.md)), you need valid values for at least some of the
variables, like an email address, a URL for the project (like the github repository) and
of course, the name variable should be the same as the package that you want to submit.
The version variable is also crucial, because you can only upload code of a given
version once. So you may have to adjust it. In any case, make sure that the name
of your package is not already taken by someone else (check on [pypi.org](https://pypi.org)). 

If you have set up the project structure
with *manati*, you are already done with all settings and ready to deploy.

## Deploy to github, gitlab, bitbucket, etc.

When you create a project with *manati*, it also creates a local git repository
on your computer. You can use it as it is, but at some point, you may want to
have your repository in the internet so that other people can see it, use it and
maybe contribute to it. *manati* can help you transferring your code to one
of the git-based platforms. 

First thing to do: go to github.com or gitlab.com or whatever and create a new
EMPTY repository there. Copy the URL for your new repository. Make sure
 you have commited your latest code changes to the local repo and then type 

```
manati deploy repo
```

*manati* will ask you for the repository URL and the name of the default branch
(depending on the platform you use, this may be *main* or *master*). After that the
code is copied to the platform and your local repository is configured to track
the remote one. So as of now you can use *git push* and *git pull* to transfer changes
between local and remote repositories.

