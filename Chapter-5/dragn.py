
#from fantasygameinvent import displayInventory
#imprting the functin but prints data frm fantasygameinvent.py fie
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory
    # your code goes here

#had t0 c0py the funcn c0de and perfect|y w0rking n0w
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v,k)
        item_total+=v
        # FILL THIS PART IN
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)