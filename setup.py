#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Pikalang setup script."""

from setuptools import setup
from pikalang import __version__

setup(
    name="pikalang",
    version=__version__,
    description="A brainfuck derivative based off the vocabulary of Pikachu.",
    license="MIT",
    keywords="esoteric programming language brainfuck",
    author="Blake Grotewold",
    author_email="hello@grotewold.me",
    url="https://github.com/grotewold/pikalang",
    py_modules=['pikalang', 'pikalang.cli',
                'pikalang.lexer', 'pikalang.parser'],
    install_requires=['ply'],
    entry_points={
        'console_scripts': [
            'pikalang = pikalang.cli:main',
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)
