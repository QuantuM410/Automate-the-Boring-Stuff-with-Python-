import re

def passdetect(passwrd) :

    rexgen = re.compile('.*')
    rexdec = re.compile('\d')
    rexlwr = re.compile('[a-z]')
    rexupr = re.compile('[A-Z]')

    givenpass = ''.join(rexgen.findall(passwrd))
    decima = ''.join(rexdec.findall(passwrd))
    lwercase = ''.join(rexlwr.findall(passwrd))
    uprcase = ''.join(rexupr.findall(passwrd))
    if decima == '' or uprcase == '' or lwercase == '' :
        print('WEAK PASSW0RD')
    elif decima in givenpass and lwercase in givenpass and uprcase in givenpass and 8 <= len(givenpass) : #ik its wrng as even if decima , abc,ABC nt in passwrd it returns strng
        print('STR0NG PASSW0RD')
    else :
        print('WEAK PASSW0RD')

pas = input()
passdetect(pas)
