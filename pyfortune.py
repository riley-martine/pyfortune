import argparse
import os
import random
import re
import sys

FORTUNES_FILES = ["myfortunes.txt"]  # Paths relative to the cwd
SCRIPT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
FF_PATHS = [os.path.join(SCRIPT_PATH, file_path) for file_path in FORTUNES_FILES]

# Get the randomest random we can random
try:
    r = random.SystemRandom()
except:
    r = random


def read_fortunes(file_paths):
    return [read_fortune(file_path) for file_path in file_paths]


def read_fortune(file_path):
    contents = ""
    # Check that all of the files are there
    if not os.path.isfile(file_path):
        print(
            "Fortunes file `{}` not found! Put file in `{}`".format(
                file_path, SCRIPT_PATH
            )
        )
        sys.exit(1)
    # Read in all database files
    try:
        with open(file_path, "r") as f:
            contents += f.read()
    except IOError as er:
        print("Cannot open fortunes file at " + file_path)
        sys.exit(1)

    fortunes = contents.split("%\n")
    fortunes_no_newlines = [x.strip() for x in fortunes]
    return [file_path, fortunes_no_newlines]


def randfortune(fortunes):
    nums_fortunes = list(map(lambda l: len(l[1]), fortunes))
    num_fortunes = sum(nums_fortunes)
    f_num = r.randint(0, num_fortunes - 1)
    for i, e in enumerate(nums_fortunes):
        if f_num <= e:
            return fortunes[i][0], fortunes[i][1][f_num]


def apply_filter(func, fortunes):
    for filesworth in fortunes:
        filesworth[1] = list(filter(func, filesworth[1]))
    return fortunes


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
        print(sum([len(forts) for file, forts in FORTUNES]))
        sys.exit(0)

    if args.all:
        print(
            "\n%\n".join(
                ["\n%\n".join([f for f in fortunes]) for file, fortunes in FORTUNES]
            )
        )
        sys.exit(0)

    if sum([len(forts) for file, forts in FORTUNES]) < 1:
        print("Add more fortunes!")
        sys.exit(1)

    COOKIE_FILE_NAME, YOUR_FORTUNE = randfortune(FORTUNES)

    if args.cookie:
        print("({})\n%".format(COOKIE_FILE_NAME))

    print(YOUR_FORTUNE)
