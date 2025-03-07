#!/usr/bin/env python
"""Main entry point using ``python -m wmirsdata``."""

import errno
import sys

import wmirsdata.cli

if __name__ == "__main__":
    try:
        wmirsdata.cli.main(sys.argv[1:])
    except KeyboardInterrupt:
        sys.exit(errno.EINTR)
