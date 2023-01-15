from pathlib import Path 
import re
s0urce_path = Path('Chapter-9/prxtxtfie')
regpattern = input()
for txts0r in s0urce_path.glob('*.txt') :
    with open(f'{txts0r}', 'r') as fie :
        regex = re.compile(f'{regpattern}')
        regse = regex.findall(fie.read())
        print(regse)


