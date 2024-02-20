#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':       # sys.argv means system arugements - e.g python myscript.py arg1 arg2 arg3
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':                          # If only command line argument is 'list',
        pyperclip.copy(str(list(mcbShelf.keys())))             # copy list representation of shelf keys
    elif sys.argv[1] in mcbShelf:                              # Otherwise, you can assume the commond line argument is a keyword
        pyperclip.copy(mcbShelf[sys.argv[1]])                  # If this keyword exists im the mcbShelf shels as a key, load the value on the clipboard

mcbShelf.close()

