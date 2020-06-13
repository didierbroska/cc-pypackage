# Template cookiecutter - Python Package

![](https://github.com/didierbroska/cc-pypackage/workflows/CI%20%28cookiecutter%29/badge.svg)

This template build from original [Cookiecutter][1] template for a Python package.

- GitHub repo: https://github.com/didierbroska/cc-pypackage/
- Documentation: **TODO: GH Pages**
- Free software: MIT License

## Features

- Testing setup with `unittest` and `python setup.py test` or `pytest`
- [GitHub Actions][2]: Ready for GiHub Actions Continuous Integration testing
- [PyTest][3]: testing: Ready to test code.
- [Pytest-cov][4] & [Coverage][5]: testing: Ready to test code with coverage (optional)
- [Tox][6] testing: Setup to easily test for Python 3.5, 3.6, 3.7, 3.8
- [MkDocs][7] docs: Documentation ready for generation with.
- [bump2version][8]: Pre-configured version bumping with a single command
- Auto-release to [PyPI][9]  when you push a new tag to master or [PyPI testing][10] deploy with specific branch named `test-deploy`.
- Command line interface using Click (optional)

[1]: https://github.com/audreyr/cookiecutter
[2]: https://help.github.com/en/actions
[3]: https://docs.pytest.org/
[4]: https://pytest-cov.readthedocs.io/
[5]: https://coverage.readthedocs.io/
[6]: https://tox.readthedocs.io/
[7]: https://www.mkdocs.org/
[8]: https://github.com/c4urself/bump2version
[9]: https://pypi.org/
[10]: https://test.pypi.org/

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher):

```sh
pip install -U cookiecutter
```

Generate a Python package project:

```sh
cookiecutter gh:didierbroska/cc-pypackage
```

Then:

- Create a repo and put it there.
- Install the dev requirements into a virtualenv. (`make install`)
- Register your project with PyPI.
- Run the GitHub Actions build when you push in `master` and deploy in PyPI when you push new tag in `master`.
- Add the documention in GitHub Pages when push to `master`.
- Release your package by pushing a new tag to `master`.

- Add a package dependencies in `setup.cfg` file that specifies the packages you will need for  your project and their versions. For more info see the [setuptools documentation about setup.cfg only project](https://setuptools.readthedocs.io/en/latest/setuptools.html#setup-cfg-only-projects).
- Activate your project [on pyup.io][11](optionnal).

[11]: https://pyup.io/

For more details, see the [cc-pypackage tutorial](https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html)**TODO : update like when doc is ok**.

