#!/usr/bin/env python
import sys

from basechem import load_env

load_env.load_env()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
