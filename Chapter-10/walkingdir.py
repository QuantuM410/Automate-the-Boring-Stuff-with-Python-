import os , shutil
from pathlib import Path

for foldername, subf, files in os.walk('Chapter-10/t0bem0ved' ) :
    print(foldername)
    print(subf)
    print(files)


        