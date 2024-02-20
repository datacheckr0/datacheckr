#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw list - Loads all keywords to clipboard
#        py.exe mcb.pyw delete <keyword> - Deletes a specific keyword
#        py.exe mcb.pyw delete - Deletes all keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':               # sys.argv means system arugements - e.g python myscript.py arg1 arg2 arg3
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':                                  # If only command line argument is 'list',
        pyperclip.copy(str(list(mcbShelf.keys())))                     # copy list representation of shelf keys
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()                                               # Clear all keywords
        pyperclip.copy('All keywords deleted.')
    elif sys.argv[1] in mcbShelf:                                      # Otherwise, you can assume the commond line argument is a keyword
        pyperclip.copy(mcbShelf[sys.argv[1]])                          # # If this keyword exists im the mcbShelf shels as a key, load the value on the clipboard

# Delete a specific keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
        pyperclip.copy(f'{sys.argv[2]} deleted.')
    else:
        pyperclip.copy(f'{sys.argv[2]} not found.')

mcbShelf.close()

