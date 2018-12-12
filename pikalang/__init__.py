#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pikalang module.

A brainfuck derivative based off the vocabulary of Pikachu from Pokemon.

Copyright (c) 2019 Blake Grotewold
"""

from __future__ import print_function

import sys
import os

from pikalang.interpreter import PikalangProgram


def load_source(file):
    if os.path.isfile(file):
        if os.path.splitext(file)[1] == ".pokeball":
            with open(file, "r") as pikalang_file:
                pikalang_data = pikalang_file.read()

            return pikalang_data

        else:
            print("pikalang: file is not a pokeball", file=sys.stderr)
            return False

    else:
        print("pikalang: file does not exist", file=sys.stderr)
        return False


def evaluate(source):
    """Run Pikalang system."""

    program = PikalangProgram(source)
    program.run()
