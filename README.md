# Pyfortune: a python fortune program
I wanted to add my own fortunes to the fortune program, and writing this seemed simpler than modifying the existing fortune.
Works with python 3.6+

## Installation
The directions for installation are as follows:

* Clone the repo somewhere on your system, for example in `~/bin/`
* Edit `myfortunes.txt` to contain the fortunes you want to see
* Add `python /path/to/pyfortune.py` to your (bashrc|zshrc|fishrc)
* Open a new shell to test everything works

## Fortune files
fortune files are in the same format as the original program:

* Start with a fortune
* End the fortune with a line reading `%\n` (where `\n` is a newline character)
* Repeat steps 1 and 2 to add your fortunes.
* The final line should be a fortune, no `%` needed after.


see `myfortunes.txt` for an example if you do not understand

## Usage
Run `python3 pyfortune.py -h` to get full help.

Run `python3 pyfortune` to get a random fortune.


Command line args:

* -s --short (filter for only short fortunes)
* -l --long  (filter for only long fortunes)
* -f --files (print all the files to be searched)
* -c --cookie (print where fortune came from)
* -m --regex (filter by python regex)


## TODO
- [x] support multiple fortune files
- [x] add 'short' and 'long' options
- [x] add 'print databases' arg
- [x] add 'regex' option
- [x] add 'cookie' option
- [x] typing
- [ ] write tests
- [ ] package as python package and distribute via PyPI
- [ ] pickle fortune files for quicker reading
- [ ] test impact of pickling
- [ ] add command line arguments
- [ ] add 'wait' argument
- [ ] add original BSD fortunes and option to use them
- [ ] add 'database' arguments (offensive, all, single)
- [ ] add 'source' arg
