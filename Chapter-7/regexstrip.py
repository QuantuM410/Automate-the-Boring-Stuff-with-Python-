import re

def regstrip(givenstr, rem0vedchar) :
    if rem0vedchar != '': #cant rem0ve empty str '' as resu|ts the same
        regex = re.compile(rem0vedchar)
        newstr = regex.sub('', givenstr)
    else :
        spacepat = re.compile('(^\s*)|(\s*$)') #start with a|| space & end with space
        newstr = spacepat.sub('', givenstr)   

    print(newstr)


a, b =  map(input().split())
regstrip(a,b)