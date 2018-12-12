#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pikalang.parser module.

The parser for pikalang tokens.

Copyright (c) 2019 Blake Grotewold
"""

from __future__ import print_function

import ply.yacc as yacc

from pikalang.lexer import PikalangLexer
from pikalang.objects.loop import Loop
from pikalang.objects.commands import Commands
from pikalang.objects.command import Command


class PikalangParser(object):
    tokens = PikalangLexer.tokens

    def __init__(self, **kwargs):
        self.lexer = PikalangLexer()
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, text):
        return self.parser.parse(text, self.lexer)

    def p_command(self, p):
        """
        command : INCREMENTBYTE
                | DECREMENTBYTE
                | DECREMENTPOINTER
                | INCREMENTPOINTER
                | OUTPUT
                | INPUT
                | loop
        """

        if isinstance(p[1], str):
            p[0] = Command(p[1])
        else:
            p[0] = p[1]

    def p_loop(self, p):
        """
        loop : JUMPFORWARD commands JUMPBACKWARD
        """
        p[0] = Loop(p[2])

    def p_commands(self, p):
        """
        commands : command
                 | commands command
        """
        if len(p) == 2:
            p[0] = Commands([p[1]])
            return

        if not p[1]:
            p[1] = Commands()

        p[1].commands.append(p[2])
        p[0] = p[1]

    def p_error(self, p):
        print("Syntax error in input:", p)
