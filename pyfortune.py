import os
import sys
import random

FORTUNES_FILE = 'myfortunes.txt'
SCRIPT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
FF_PATH = os.path.join(SCRIPT_PATH, FORTUNES_FILE)

if not os.path.isfile(FF_PATH):
    print("Fortunes file not found! Put file in " + SCRIPT_PATH)
    sys.exit(1)

try:
    FF_CONTENTS = open(FF_PATH, 'r').read()
except IOError as er:
    print("Cannot open fortunes file at " + FF_PATH)
    sys.exit(1)

FORTUNES = FF_CONTENTS.split("%\n")
FORTUNES_NO_NEWLINES = list(map(lambda x: x.strip(), FORTUNES))

if len(FORTUNES_NO_NEWLINES) < 1:
    print("Add more fortunes!")

try:
    r = random.SystemRandom()
except:
    r = random

YOUR_FORTUNE = FORTUNES_NO_NEWLINES[r.randint(0, len(FORTUNES_NO_NEWLINES) - 1)]

print(YOUR_FORTUNE)

