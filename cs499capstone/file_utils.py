#!/usr/bin/env python3
import os
import logging
import yaml
import __main__


__all__ = ["here", "load_yml_file"]

here = os.path.abspath(os.path.dirname(__main__.__file__))

_log = logging.getLogger(__name__)


def load_yml_file(filename):
    loc = os.path.join(here, filename)
    if os.path.exists(loc):
        with open(loc, "r") as f:
            return yaml.full_load(f)
    raise FileNotFoundError


def main():
    print(load_yml_file(os.path.join(here, "local_config.yml")))


if __name__ == "__main__":
    main()
