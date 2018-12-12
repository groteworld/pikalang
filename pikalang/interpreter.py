from __future__ import print_function

import sys
import ply.yacc as yacc
import ply.lex as lex

tokens = (
    "INCREMENT",
    "DECREMENT",
    "SHIFT_LEFT",
    "SHIFT_RIGHT",
    "OUTPUT",
    "INPUT",
    "OPEN_LOOP",
    "CLOSE_LOOP",
)

t_INCREMENT = r"pi"
t_DECREMENT = r"ka"
t_SHIFT_LEFT = r"pipi"
t_SHIFT_RIGHT = r"pichu"
t_OUTPUT = r"pikachu"
t_INPUT = r"pikapi"
t_OPEN_LOOP = r"pika"
t_CLOSE_LOOP = r"chu"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " \t"


def t_error(t):
    t.lexer.skip(1)


def p_commands(p):
    """
    commands : command
             | commands command
    """
    if len(p) == 2:
        p[0] = Commands()
        p[0].commands = [p[1]]
        return

    if not p[1]:
        p[1] = Commands()

    p[1].commands.append(p[2])
    p[0] = p[1]


def p_command(p):
    """
    command : INCREMENT
            | DECREMENT
            | SHIFT_LEFT
            | SHIFT_RIGHT
            | OUTPUT
            | INPUT
            | loop
    """
    if isinstance(p[1], str):
        p[0] = Command(p[1])
    else:
        p[0] = p[1]


def p_loop(p):
    """
    loop : OPEN_LOOP commands CLOSE_LOOP
    """
    p[0] = Loop(p[2])


def p_error(p):
    print("Syntax error in input!")


class PikalangProgram:
    def __init__(self, source):
        self.source = source

    def run(self):
        self.data = [0] * 20
        self.location = 0
        commands = self.parse(self.source)
        commands.run(self)

    def parse(self, source):
        lexer = lex.lex()
        parser = yacc.yacc(debug=False, write_tables=False)
        return parser.parse(source)

    def __str__(self):
        return str(self.parse(self.source))


class Commands:
    def __init__(self):
        self.commands = []

    def run(self, program):
        for command in self.commands:
            command.run(program)

    def __str__(self):
        return "".join([str(command) for command in self.commands])


class Command:
    def __init__(self, command):
        self.command = command

    def run(self, program):
        if isinstance(self.command, Loop):
            self.command.run(program)

        if self.command == t_INCREMENT:
            program.data[program.location] += 1
        if self.command == t_DECREMENT:
            program.data[program.location] -= 1
        if self.command == t_SHIFT_LEFT:
            program.location -= 1
        if self.command == t_SHIFT_RIGHT:
            program.location += 1
        if self.command == t_OUTPUT:
            sys.stdout.write(chr(program.data[program.location]))

    def __str__(self):
        return self.command


class Loop:
    def __init__(self, commands):
        self.commands = commands

    def run(self, program):
        while program.data[program.location] != 0:
            self.commands.run(program)

    def __str__(self):
        return t_OPEN_LOOP + str(self.commands) + t_CLOSE_LOOP
