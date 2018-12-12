#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pikalang.lexer module.

The lexer for pikalang.

Copyright (c) 2019 Blake Grotewold
"""

from __future__ import print_function

import ply.lex as lex


class PikalangLexer(object):
    tokens = (
        "DECREMENTPOINTER",
        "INCREMENTPOINTER",
        "OUTPUT",
        "INPUT",
        "INCREMENTBYTE",
        "DECREMENTBYTE",
        "JUMPFORWARD",
        "JUMPBACKWARD",
        "IGNORE",
    )

    # Regular expression rules for tokens
    t_DECREMENTPOINTER = r"pichu"
    t_INCREMENTPOINTER = r"pipi"
    t_OUTPUT = r"pikachu"
    t_INPUT = r"pikapi"
    t_INCREMENTBYTE = r"pi"
    t_DECREMENTBYTE = r"ka"
    t_JUMPFORWARD = r"pika"
    t_JUMPBACKWARD = r"chu"
    t_IGNORE = r"[ \t]+"

    def t_newline(self, t):
        r"[\n\r]+"
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print("Illegal character: {}".format(t.value[0]))
        t.lexer.skip(1)

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.lexer.linestart = 0

    def __iter__(self):
        return iter(self.lexer)

    def token(self):
        return self.lexer.token()

    def input(self, data):
        self.lexer.input(data)

     def test(self,data):
         self.lexer.input(data)
         while True:
              tok = self.lexer.token()
              if not tok:
                  break
              print(tok)
