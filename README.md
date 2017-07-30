#Pyfortune: a python fortune program
I wanted to add my own fortunes to the fortune program, and writing this seemed simpler than modifying the existing fortune.

##Installation
* Clone the repo somewhere on your system, maybe in `~/bin/`
* Edit `myfortunes.txt` to only contain the fortunes you want to see
* Add `python /path/to/pyfortune.py` to your (bashrc|zshrc|fishrc)
* Open a new shell to test everything works

##Fortune files
fortune files are in the same format as the original program:

* Start with a fortune
* End the fortune with a line containing only `%\n`
* Repeat steps 1 and 2 n times
* End the file with only a fortune, no `%`


see `myfortunes.txt` for an example if you do not understand

##TODO
- [ ] support multiple fortune files
- [ ] package as python package and distribute via PyPI
- [ ] pickle fortune files for quicker reading
- [ ] test impact of pickling
- [ ] add command line arguments
- [ ] add 'wait' argument
- [ ] add original BSD fortunes and option to use them
- [ ] add 'short' and 'long' options
- [ ] add 'regex' option
- [ ] add 'database' arguments (offensive, all, single)
- [ ] add 'source' arg
- [ ] add 'print databases' arg
