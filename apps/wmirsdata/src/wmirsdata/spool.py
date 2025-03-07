"""Continuously processes files added to a spool in directory."""

import logging
import pathlib
import time

from .validate import validate_file

logger = logging.getLogger(__name__)


def spool_start(args):
    """Start the spool processing loop."""

    # pylint: disable=bare-except

    logger.info("Create spool directories")
    args.input.mkdir(parents=True, exist_ok=True)
    args.output.mkdir(parents=True, exist_ok=True)
    args.error.mkdir(parents=True, exist_ok=True)

    logger.info("Clean output (%s) and error (%s) directories", args.output, args.error)

    logger.info("Start processing files in %s", args.input)
    while True:
        time.sleep(1.0)
        for path_in in args.input.iterdir():
            logger.debug("Start processing %s", path_in)
            if not path_in.is_file(follow_symlinks=False):
                logger.debug("Path is not a file %s", path_in)
                continue
            if path_in.suffix not in [".csv"]:
                logger.debug("Skipping non CSV file %s", path_in)
                continue
            path_out = args.output / path_in.with_suffix(".json").name
            path_err = args.error / path_in.name
            logger.debug(
                "Process %s from %s to %s with error %s",
                path_in.name,
                path_in,
                path_out,
                path_err,
            )
            try:
                validate_file(path_in, path_out, path_err)
            except:
                logger.exception("Problem with file %s", path_err.name)
                path_out.unlink(missing_ok=True)
            else:
                path_err.unlink(missing_ok=True)
            finally:
                path_in.unlink(missing_ok=True)
                logger.info("Processed %s", path_in)


def spool(subparsers):
    """Subparser for the spool command."""
    parser = subparsers.add_parser("spool", help=__doc__)
    parser.set_defaults(func=spool_start)
    parser.add_argument(
        "--input",
        help="Input spool directory (default: ./data/in)",
        type=pathlib.Path,
        default=pathlib.Path("./data/in"),
    )
    parser.add_argument(
        "--output",
        help="Output directory (default: ./data/out)",
        type=pathlib.Path,
        default=pathlib.Path("./data/out"),
    )
    parser.add_argument(
        "--error",
        help="Error directory (default: ./data/err)",
        type=pathlib.Path,
        default=pathlib.Path("./data/err"),
    )
