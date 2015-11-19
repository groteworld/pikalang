#!/usr/bin/python
# -*- coding: utf-8 -*-
"""pikalang.lexer

The lexer for pikalang.

Copyright (c) 2015 Blake Grotewold
"""

import ply.lex as lex


class PikalangLexer:
    """Token lexer for Pikalang."""

    # List of token names
    tokens = (
        'DECREMENTPOINTER',
        'INCREMENTPOINTER',
        'OUTPUT',
        'INPUT',
        'INCREMENTBYTE',
        'DECREMENTBYTE',
        'JUMPFORWARD',
        'JUMPBACKWARD',
        'COMMENT'
    )

    # Regular expression rules for tokens
    t_DECREMENTPOINTER = r'\bpichu\b'
    t_INCREMENTPOINTER = r'\bpipi\b'
    t_OUTPUT = r'\bpikachu\b'
    t_INPUT = r'\bpikapi\b'
    t_INCREMENTBYTE = r'\bpi\b'
    t_DECREMENTBYTE = r'\bka\b'
    t_JUMPFORWARD = r'\bpika\b'
    t_JUMPBACKWARD = r'\bchu\b'
    t_COMMENT = r'[^\s]+'

    t_ignore = ' \t\n\r'

    def t_newline(self, t):
        """Token for line numbers.

        This allows us to keep track of what line number for error reporting.
        """
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        """Error handling rule."""
        print("Illegal character {}".format(t.value[0]))
        t.lexer.skip(1)

    def __init__(self, **kwargs):
        """Build the lexer."""
        self.lexer = lex.lex(module=self, **kwargs)

    def load(self, data):
        """Load data into lexer.

        Returns list of tokens.
        """
        self.lexer.input(data)
