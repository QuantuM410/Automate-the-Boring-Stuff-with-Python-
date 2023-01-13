import pyinputplus as pyp
import random, time
print('Multiplication Quiz'.center(20)) 
crrect = 0
for i in range(1,11) :
    try :
        n1 , n2 = random.randint(0,9) , random.randint(0,9)
        print('#%s %s x %s ' % (i, n1 , n2))
        pyp.inputStr(prompt = 'Enter Ur Answer : '.rjust(5) , allowRegexes=['^%s$' % (n1*n2)] , blockRegexes=[('.*', '\033[1m'+'INC0RRECT!'+'\033[0m')] , limit=3 , timeout=8)
    except pyp.TimeoutException :
        print('\033[1m'+'Timed 0ut'+'\033[0m')
    except pyp.RetryLimitException :
        print('\033[1m'+'N0 m0re tries'+'\033[0m')
    else :
        crrect += 1
        print('\033[1m'+'C0RRECT!'.rjust(5)+'\033[0m')
    time.sleep(1)

print('\033[1m'+'Score: %s / 10' % (crrect) + '\033[0m') #t0 b0Id text

