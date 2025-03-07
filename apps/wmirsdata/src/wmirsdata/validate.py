"""Validate a single file."""

import argparse
import csv
import logging
import sys

logger = logging.getLogger(__name__)


def validate_stream(file_in, file_out, file_err):
    """Validate stdin and convert onto stdout or errors onto stderr."""

    # pylint: disable=unused-argument

    reader = csv.DictReader(file_in)
    for row in reader:
        print(row)


def validate_file(path_in, path_out, path_err):
    """Validate the file at `path_in` and convert into `path_out` or `path_err`."""
    with (
        path_in.open("rt") as stream_in,
        path_out.open("wt") as stream_out,
        path_err.open("wt") as stream_err,
    ):
        validate_stream(stream_in, stream_out, stream_err)


def validate(subparsers):
    """Subparser for the validate command."""

    def handle_cli(args):
        validate_stream(args.file, args.output, sys.stderr)

    parser = subparsers.add_parser("validate", help=__doc__)
    parser.set_defaults(func=handle_cli)
    parser.add_argument(
        "file",
        help="File to validate (default: stdin)",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file path (default: stdout)",
        type=argparse.FileType("w"),
        default=sys.stdout,
    )
