#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pikalang.objects.command module.

The Command class used in pikalang

Copyright (c) 2019 Blake Grotewold
"""
import sys

from pikalang.lexer import PikalangLexer
from pikalang.objects.loop import Loop

MAX_LOCATIONS = 20


class Command:
    """A single command to be run."""

    def __init__(self, command):
        self.command = command

    def run(self, program):
        if isinstance(self.command, Loop):
            self.command.run(program)

        if self.command == PikalangLexer.t_INCREMENTBYTE:
            program.data[program.location] += 1
        if self.command == PikalangLexer.t_DECREMENTBYTE:
            program.data[program.location] -= 1
        if self.command == PikalangLexer.t_DECREMENTPOINTER:
            program.location -= 1
            if program.location > 0:
                program.location = MAX_LOCATIONS - 1
        if self.command == PikalangLexer.t_INCREMENTPOINTER:
            program.location = (program.location + 1) % MAX_LOCATIONS
        if self.command == PikalangLexer.t_OUTPUT:
            sys.stdout.write(chr(program.data[program.location]))

    def __str__(self):
        return self.command
