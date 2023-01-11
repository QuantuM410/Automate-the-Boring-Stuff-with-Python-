def tabprinter(tableData) :
    colWidths = [0] * len(tableData)
    max = 0
    for k,i in enumerate(tableData) :
        for j in i :
            if max < len(j) :
                max = len(j)
        colWidths[k] = max
        max = 0
    for m in range(len(tableData[0])) :
        for n in range(len(tableData)) :
            print(tableData[n][m].rjust(colWidths[n]), end = ' ')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
tabprinter(tableData)
    