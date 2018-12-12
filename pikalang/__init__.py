#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pikalang module.

A brainfuck derivative based off the vocabulary of Pikachu from Pokemon.

Copyright (c) 2019 Blake Grotewold
"""

from pikalang.parser import PikalangParser


class PikalangProgram:
    def __init__(self, source):
        self.source = source

    def run(self):
        self.data = [0] * 20
        self.location = 0
        commands = self.parse(self.source)
        commands.run(self)

    def parse(self, source):
        parser = PikalangParser()
        return parser.parse(source)

    def __str__(self):
        return str(self.parse(self.source))

def evaluate(source):
    """Run Pikalang system."""

    program = PikalangProgram(source)
    program.run()
