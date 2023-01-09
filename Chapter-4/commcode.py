def comma(lst):
    str= ''
    for i,j in enumerate(lst) :
        if i != len(lst) -1 :
            str = str + j + ', '
        else : 
            str = str + 'and ' + j 
    return str

test = input().split()

print(comma(test))
