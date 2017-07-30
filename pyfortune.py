import os
import sys
import random

FORTUNES_FILES = ['myfortunes.txt']
SCRIPT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
FF_PATHS = [os.path.join(SCRIPT_PATH, file_path) for file_path in FORTUNES_FILES] 


def read_files(paths):
  contents = ""
  for file_path in paths:
    # Check that all of the files are there
    if not os.path.isfile(file_path):
      print("Fortunes file `{}` not found! Put file in `{}`".format(file_path,  SCRIPT_PATH))
      sys.exit(1)
    # Read in all database files
    try:
      contents += open(file_path, 'r').read()
    except IOError as er:
      print("Cannot open fortunes file at " + file_path)
      sys.exit(1)
  return contents


# Pull fortunes out of files
CONTENTS = read_files(FF_PATHS)
FORTUNES = CONTENTS.split("%\n")
FORTUNES_NO_NEWLINES = [x.strip() for x in FORTUNES]

if len(FORTUNES_NO_NEWLINES) < 1:
  print("Add more fortunes!")

# Get the randomest random we can random
try:
  r = random.SystemRandom()
except:
  r = random

# Select a random fortune from all the fortunes
YOUR_FORTUNE = FORTUNES_NO_NEWLINES[r.randint(0, len(FORTUNES_NO_NEWLINES) - 1)]

print(YOUR_FORTUNE)

