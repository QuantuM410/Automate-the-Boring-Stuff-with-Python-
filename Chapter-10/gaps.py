import os, re
for i in range(10) : #creating 10 fi|es
    path = 'Chapter-10/GAP/'+ 'spam' + f'{i}'
    print(path)
    with open(path, 'w') as fie :
        fie.close()

for f, sf, fs in os.walk('Chapter-10/GAP/') :
    print(fs)
    for fss in fs :
        patmatch = re.search('spam?', fss)
        if patmatch :
            print(fss)


