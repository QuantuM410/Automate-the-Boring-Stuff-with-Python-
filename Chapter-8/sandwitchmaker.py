import pyinputplus as pyp
prices = {'wheat' : 5, 'white' : 3, 'sourdough' : 4, 'Chicken' : 8, 'Ham' : 10, 'Tofu' : 6, 'Turkey' : 20, 'cheddar' : 2, 'swiss' : 4, 'mozzarella' : 5}
cst = 0
breadtype = pyp.inputMenu(['wheat', 'white', 'sourdough'] , numbered = True)
prteintype = pyp.inputMenu(['Chicken', 'Ham', 'Tofu', 'Turkey'] , numbered = True)
sandcount = pyp.inputInt(prompt = 'how many sandwiches you want?', min = 1)
yescheese = pyp.inputYesNo(prompt = 'Do You Want Cheese')
if yescheese == 'yes' :
    cheesetype = pyp.inputMenu(['cheddar','swiss', 'mozzarella'] , numbered = True)
    print('T0TAl Cost is ', sandcount * (prices[breadtype] + prices[prteintype] + prices[cheesetype]) )

else :
    print('T0TAl Cost is ', sandcount * (prices[breadtype] + prices[prteintype]), '$')




