
def isValidChessBoard(chess_b):
    n=0
    pawns = [['bpawn', 'bknight', 'bqueen', 'bking', 'brook', 'bbishop'],
             ['wpawn', 'wknight', 'wqueen', 'wking', 'wrook', 'wbishop']]
    positions = [['1','2','3','4','5','6','7','8'],['a','b','c','d','e','f','g','h']]
    black = 0
    white = 0
    bkingcount = 0
    wkingcount = 0
    for k,v in chess_b.items() :
        if v in pawns[0] :
            black += 1
            if v == 'bking' :
                bkingcount+=1
                if 1 < bkingcount :
                    n=1
                    break
            if 16 < black :
                n=1
                break
        if v in pawns[1] :
            white += 1
            if v == 'wking' :
                wkingcount+=1
                if 1 < wkingcount :
                    n=1
                    break
            if 16 < white :
                n=1
                break

        if v not in pawns[0] and v not in pawns[1] :
            n=1
            break
        if k[0] not in positions[0] or k[1] not in positions[1] :
            n=1
            break

    if n == 1:
        return False
    else :
        return True

b = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(b))

        

            
