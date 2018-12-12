#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pikalang.objects.commands module.

A collection of Command classes used in pikalang

Copyright (c) 2019 Blake Grotewold
"""


class Commands:
    """A collection of command objects to run."""

    def __init__(self, commands=[]):
        self.commands = commands

    def run(self, program):
        for command in self.commands:
            command.run(program)

    def __str__(self):
        return "".join([str(command) for command in self.commands])
