import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
HT = {'0' : 'tails', '1' : 'heads'}
toss = HT[str(random.randint(0, 1))] # 0 is tails, 1 is heads
if toss == guess.lower():
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guesss.lower():
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')