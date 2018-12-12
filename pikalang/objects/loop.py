#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pikalang.objects.loop module.

The Loop classes used in pikalang

Copyright (c) 2019 Blake Grotewold
"""

from pikalang.lexer import PikalangLexer


class Loop:
    """An iterative loop of commands."""

    def __init__(self, commands):
        self.commands = commands

    def run(self, program):
        while program.data[program.location] != 0:
            self.commands.run(program)

    def __str__(self):
        return (
            PikalangLexer.t_JUMPFORWARD
            + str(self.commands)
            + PikalangLexer.t_JUMPBACKWARD
        )
