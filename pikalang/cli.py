#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pikalang.cli module.

Command Line Interface to pikalang.

Copyright (c) 2019 Blake Grotewold
"""

from __future__ import print_function

import os
import sys
import argparse
import setup

import pikalang


def main():
    """Run application as a CLI executable"""
    arg_parser = argparse.ArgumentParser(
        prog="pikalang",
        description="a Pikalang interpreter written in Python",
        argument_default=argparse.SUPPRESS,
    )

    arg_parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s {0}".format(setup.__VERSION__)
    )
    arg_parser.add_argument("file", help="the path to the pokeball file")

    args = arg_parser.parse_args()

    if os.path.isfile(args.file):
        if os.path.splitext(args.file)[1] == ".pokeball":
            with open(args.file, "r") as pikalang_file:
                pikalang_data = pikalang_file.read()

            pikalang.evaluate(pikalang_data)

        else:
            arg_parser.print_usage()
            print("pikalang: file is not a pokeball", file=sys.stderr)

    else:
        arg_parser.print_usage()
        print("pikalang: file does not exist", file=sys.stderr)


if __name__ == "__main__":
    main()
