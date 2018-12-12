#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pikalang.cli module.

Command Line Interface to pikalang.

Copyright (c) 2019 Blake Grotewold
"""

from __future__ import print_function

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
        "-v",
        "--version",
        action="version",
        version="%(prog)s {0}".format(setup.__VERSION__),
    )
    arg_parser.add_argument("file", help="the path to the pokeball file")

    args = arg_parser.parse_args()

    sourcecode = pikalang.load_source(args.file)

    if sourcecode:
        pikalang.evaluate(sourcecode)
    else:
        arg_parser.print_usage()


if __name__ == "__main__":
    main()
