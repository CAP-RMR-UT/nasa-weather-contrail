"""Validate and transform files for upload to Civil Air Patrol WMIRS"""

import argparse
import logging
import sys

from .spool import spool
from .validate import validate


def main(argv=None):
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-v",
        "--verbose",
        help="set logging level",
        choices=["warning", "info", "debug"],
        default="info",
    )
    subparsers = parser.add_subparsers(help="Subcommands")
    spool(subparsers)
    validate(subparsers)
    args = parser.parse_args(args=argv)
    logging.basicConfig(level=args.verbose.upper())
    try:
        args.func(args)
    except AttributeError as err:
        if err.args[0] == "'Namespace' object has no attribute 'func'":
            parser.print_help()
            sys.exit(1)
        else:
            raise err
