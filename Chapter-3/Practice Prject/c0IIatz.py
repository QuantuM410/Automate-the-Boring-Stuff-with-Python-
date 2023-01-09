def collatz(number):
    if number%2 == 0:
        number = number // 2
    else :
        number = 3 * number + 1
    return(number)

try:
    numberbyuser = int(input())
    while numberbyuser != 1 :
        numberbyuser = collatz(numberbyuser)
        print(numberbyuser)
        
except ValueError:
    print('Please enter an integer')


