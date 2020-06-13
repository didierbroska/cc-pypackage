# !/usr/bin/env python
# coding: utf-8

"""
Setup script
"""

from setuptools import setup

setup_kwargs = dict(
        test_suite='test'
        )

try:
    setup(
        **setup_kwargs
        )
except LookupError:
    # This means the source code was not from git or PyPI
    setup(
        version='0.1.0',
        **setup_kwargs
        )
