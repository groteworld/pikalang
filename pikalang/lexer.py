#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pikalang.lexer module.

The lexer for pikalang.

Copyright (c) 2019 Blake Grotewold
"""

import ply.lex as lex

class PikalangLexer(object):
    """Token lexer for Pikalang."""

    tokens = (
        "DECREMENTPOINTER",
        "INCREMENTPOINTER",
        "OUTPUT",
        "INPUT",
        "INCREMENTBYTE",
        "DECREMENTBYTE",
        "JUMPFORWARD",
        "JUMPBACKWARD",
        "COMMENT",
        "IGNORE",
    )

    def __init__(self, **kwargs):
        """Build the lexer."""
        self.lexer = lex.lex(module=self, **kwargs)
        self.lexer.linestart = 0

    # Regular expression rules for tokens
    t_DECREMENTPOINTER = r"pichu"
    t_INCREMENTPOINTER = r"pipi"
    t_OUTPUT = r"pikachu"
    t_INPUT = r"pikapi"
    t_INCREMENTBYTE = r"pi"
    t_DECREMENTBYTE = r"ka"
    t_JUMPFORWARD = r"pika"
    t_JUMPBACKWARD = r"chu"
    t_COMMENT = r"[^\s]+"

    t_IGNORE = "[ \t\n\r]"

    def t_newline(self, t):
        """Token for line numbers.

        This allows us to keep track of what line number for error reporting.
        """
        r"\n+"
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        """Error handling rule."""
        print("Illegal character {}".format(t.value[0]))
        t.lexer.skip(1)

    def __iter__(self):
        return iter(self.lexer)

    def token(self):
        return self.lexer.token()

    def input(self, data):
        self.lexer.input(data)