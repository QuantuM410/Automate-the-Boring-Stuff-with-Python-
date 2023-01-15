#! python3
# python mcb.pyw save {keyw0rd}
# python mcb.pyw {keyw0rd}
# python mcb.pyw list 
# python mcb.pyw de|ete {keyw0rd}
# mcb.py - A multi-clipboard program.

import pyperclip, sys, shelve

mcbShelf = shelve.open('mcb')


if len(sys.argv) == 3 and sys.argv[1].lower() == 'save': 
    mcbShelf[sys.argv[2]] = pyperclip.paste() 

if len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    pyperclip.copy('')

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf:
    pyperclip.copy(str(list(mcbShelf.keys()).remove(sys.argv[2])))

elif len(sys.argv) == 2: 
    if sys.argv[1].lower() == 'list':  
        pyperclip.copy(str(list(mcbShelf.keys()))) 

    elif sys.argv[1] in mcbShelf: 
        pyperclip.copy(mcbShelf[sys.argv[1]])

    
mcbShelf.close()