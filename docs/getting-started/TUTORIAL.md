# Tutorial

To start with, you will need a [GitHub Account][1] and un account on [PyPI][2]. Create these before you get started on this tutorial.

[1]: https://github.com/
[2]: https//pypi.python.org/pypi

> It's possible to test deployement with [PyPI Test][9]

## Step 1: Install Cookiecutter

First, you need to create and activate a virtualenv for the package project. Use your favorite method, or create a pyenv-virtualenv for your new package like this:

```bash
pyenv vitualenv <python-version> <my-project>
```

Here `<your-env>` is the name of the package that you'll create. *Or you can use another name, if you want.*

Activate your environment:

```bash
pyenv activate <my-project>
```

Install cookiecutter:

```bash
pip install cookiecutter
```

## Step 2: Generate Your Package

Use `cookiecutter`, pointing it at the cookiecutter-pypackage repo:

```bash
cookiecutter gh:didierbroska/cookiecutter-pypackage
```

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, stick with the defaults.

## Step 3: Create a GitHub Repo

Enter in your new folder project named by `cookiecutter`, and create a `git` base, tracked all files et make your first commit and push to create a new repo. This is so that GitHub Actions and pyup.io can find it when we get to Step 5 and Step 7.

```bash
cd <my-project>
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:<your-gh-account-name>/<your-project>.git
git push -u origin master
```

To create a repository, you'll need a ssh key to push the repo. you can [generate][3] a key and/or [add][4] an existing one.

[3]: https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key
[4]: https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent

## Step 4: Install Dev Requirement

Your virtualenv should still be activated. If it isn't, activate it now. Install the new project's local developpement requirements:

**For pyenv user**

[`Pyenv`][5] allows to create a local environnment which loading when you enter on the folder.

[5]: https://github.com/pyenv/pyenv

```bash
pyenv local <my-project> <version-python-1> <version-python-N>
```

> `<version-python>` permits to handle test others version with tox. You'll see it at the **TODO**.

You should still b in the folder containing the `setup.cfg` file.

```bash
make develop
# or you don't use make
pip install -e '.[dev]'
```

## Step 5: Set Up GitHub Actions

[GitHub Actions][6] is a continous integration tool integrated at GiHub used to prevent intregration problems. Every commit to the master branch will trigger automated builds of the application.

Before running `Actions`, you must be create a [`Secret`][7] with your [token][8] from your PyPI account. 

> If you want trying deployement you can use [PyPI Test][9] before.

[6]: https://help.github.com/en/actions
[7]: https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets
[8]: https://pypi.org/help/#apitoken
[9]: https://test.pypi.org/

## Step 6: Set Up Mkdocs / GitHub Pages

In this template, the documents generator is [MkDocs][10]

[10]: https://www.mkdocs.org/
