#!/usr/bin/env python3
"""Python implementation of the fortune program. Prints random fortune."""
import argparse
import os
import random
import re
import sys
from typing import List, Tuple

FORTUNES_FILES = ["myfortunes.txt"]  # Paths relative to the cwd
SCRIPT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
FF_PATHS = [os.path.join(SCRIPT_PATH, file_path) for file_path in FORTUNES_FILES]


def read_fortune_file(file_path: str) -> List[str]:
    """Get the fortunes in a fortune file."""
    # Check that all of the files are there
    if not os.path.isfile(file_path):
        print(f"Fortunes file `{file_path}` not found! Put file in `{SCRIPT_PATH}`")
        sys.exit(1)
    # Read in all database files
    try:
        with open(file_path, "r") as fortunes_file:
            contents = fortunes_file.read()
    except IOError:
        print("Cannot open fortunes file at " + file_path)
        sys.exit(1)

    return [fortune.strip() for fortune in contents.split("%\n")]


def read_fortunes(file_paths: List[str]) -> List[Tuple[str, str]]:
    """Get a list of (cookie_file, fortune) for each fortune."""
    fortunes = []
    for file_path in file_paths:
        fortunes.extend(
            [(file_path, fortune) for fortune in read_fortune_file(file_path)]
        )
    return fortunes


def rand_fortune(fortunes: List[Tuple[str, str]]) -> Tuple[str, str]:
    """Pick a random fortune from a list."""
    return random.choice(fortunes)


def apply_filter(func, fortunes: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """Get only fortunes where func(fortune) is True."""
    return [fortune for fortune in fortunes if func(fortune[1])]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python implementation of `fortune` program"
    )
    parser.add_argument(
        "-s",
        "--short",
        help="Print a fortune at most 160 characters in length",
        action="store_true",
    )
    parser.add_argument(
        "-l",
        "--long",
        help="Print a fortune at least 160 characters in length",
        action="store_true",
    )
    parser.add_argument(
        "-f",
        "--files",
        help="Print a list of files that will be searched",
        action="store_true",
    )
    parser.add_argument(
        "-c",
        "--cookie",
        help="Also print the cookie file the fortune came from",
        action="store_true",
    )
    parser.add_argument(
        "-m",
        "--regex",
        help="Filter fortunes by regex pattern. Uses python's regex syntax.",
    )
    parser.add_argument(
        "-n",
        "--number",
        help="Print the number of fortunes matching the criteria given.",
        action="store_true",
    )
    parser.add_argument(
        "-a",
        "--all",
        help="Print all fortunes matching criteria given.",
        action="store_true",
    )
    args = parser.parse_args()
    # print(args)

    # Pull fortunes out of files

    if args.files:
        for file in FORTUNES_FILES:
            print(file)
        sys.exit(0)

    FORTUNES = read_fortunes(FF_PATHS)
    if args.short and args.long:
        print("Error: Fortunes cannot be both short and long!")
        sys.exit(1)
    if args.short:
        FORTUNES = apply_filter(lambda x: len(x) <= 160, FORTUNES)
    if args.long:
        FORTUNES = apply_filter(lambda x: len(x) >= 160, FORTUNES)
    if args.regex:
        prog = re.compile(args.regex)
        FORTUNES = apply_filter(prog.match, FORTUNES)

    if args.number:
        print(len(FORTUNES))
        sys.exit(0)

    if args.all:
        print("\n%\n".join([fortune for _, fortune in FORTUNES]))
        sys.exit(0)

    if len(FORTUNES) < 1:
        print("Add more fortunes!")
        sys.exit(1)

    COOKIE_FILE_NAME, YOUR_FORTUNE = rand_fortune(FORTUNES)

    if args.cookie:
        print("({})\n%".format(COOKIE_FILE_NAME))

    print(YOUR_FORTUNE)
