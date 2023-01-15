import os , shutil, re
from pathlib import Path

m0ving = Path('Chapter-10/t0bem0ved')
destin = Path('Chapter-10/m0ved')

for fder, subf, fies in os.walk('Chapter-10/t0bem0ved') :
    for fie in fies :
        match = re.search('\.*' , fie)
        if match :
            print('Chapter-10/t0bem0ved'+'/'+fie , 'Chapter-10/m0ved')
            shutil.copy('Chapter-10/t0bem0ved'+'/'+fie , 'Chapter-10/m0ved')


    


        