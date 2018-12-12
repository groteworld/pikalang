#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pikalang.objects.command module.

The Command class used in pikalang

Copyright (c) 2019 Blake Grotewold
"""
import sys

from pikalang.objects.loop import Loop

from pikalang.rules import (
    t_INCREMENTBYTE,
    t_INCREMENTPOINTER,
    t_DECREMENTBYTE,
    t_DECREMENTPOINTER,
    t_OUTPUT,
)


class Command:
    """A single command to be run."""

    def __init__(self, command):
        self.command = command

    def run(self, program):
        if isinstance(self.command, Loop):
            self.command.run(program)

        if self.command == t_INCREMENTBYTE:
            program.data[program.location] += 1
        if self.command == t_DECREMENTBYTE:
            program.data[program.location] -= 1
        if self.command == t_DECREMENTPOINTER:
            program.location -= 1
        if self.command == t_INCREMENTPOINTER:
            program.location += 1
        if self.command == t_OUTPUT:
            sys.stdout.write(chr(program.data[program.location]))

    def __str__(self):
        return self.command
