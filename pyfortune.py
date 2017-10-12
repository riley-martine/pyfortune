import os
import sys
import random
import argparse

FORTUNES_FILES = ['myfortunes.txt']
SCRIPT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
FF_PATHS = [os.path.join(SCRIPT_PATH, file_path) for file_path in FORTUNES_FILES] 

# Get the randomest random we can random
try:
  r = random.SystemRandom()
except:
  r = random

def read_fortunes(paths):
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

  fortunes = contents.split("%\n")
  fortunes_no_newlines = [x.strip() for x in fortunes]
  return fortunes_no_newlines

def randfortune(fortunes):
   return r.choice(fortunes)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Python implementation of `fortune` program")
  parser.add_argument("-s", "--short", help="Print a fortune at most 160 characters in length", action='store_true')
  parser.add_argument("-l", "--long", help="Print a fortune at least 160 characters in length", action='store_true')
  args = parser.parse_args()
  # print(args)



  # Pull fortunes out of files
  FORTUNES = read_fortunes(FF_PATHS)
  
  if args.short:
    FORTUNES = list(filter(lambda x: len(x) <= 160, FORTUNES))
  if args.long:
    FORTUNES = list(filter(lambda x: len(x) >= 160, FORTUNES))
    

  if len(FORTUNES) < 1:
    print("Add more fortunes!")
    sys.exit(1)
  
  YOUR_FORTUNE = randfortune(FORTUNES)
  
  print(YOUR_FORTUNE)

