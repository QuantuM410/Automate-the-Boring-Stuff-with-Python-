import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    list = []
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100) : 
        val = random.randint(0,1)
        if val == 0 :
            list.append('H')
        else :
            list.append('T')
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for j in range(95) :
        if list[j] == list[j+1] == list[j+2] == list[j+3] == list[j+4] == list[j+5] :
            numberOfStreaks+=1
        
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))