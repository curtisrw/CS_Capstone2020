#!/usr/bin/env python3

# STD
import logging

# PIP

# LOCAL
from file_utils import load_yml_file
from arguments import BaseArgParser

_log = logging.getLogger()


def main(argv):
    config = load_yml_file(argv.config)


if __name__ == "__main__":
    parser = BaseArgParser()
    ARGV = parser.parse_args()
    main(ARGV)
