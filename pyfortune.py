import os
import sys
import random

FORTUNES_FILES = ['myfortunes.txt']
SCRIPT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
FF_PATHS = [os.path.join(SCRIPT_PATH, file_path) for file_path in FORTUNES_FILES] 

for file_path in FF_PATHS:
  if not os.path.isfile(file_path):
      print("Fortunes file `{}` not found! Put file in `{}`".format(file_path,  SCRIPT_PATH))
      sys.exit(1)

FF_CONTENTS = ""
for file_path in FF_PATHS:
  try:
      FF_CONTENTS += open(file_path, 'r').read()
  except IOError as er:
      print("Cannot open fortunes file at " + file_path)
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

