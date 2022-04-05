realarray = [[2,4,5,1],
             [3,0,2,1],
             [2,4,5,1],
             [3,0,2,7],
             [4,3,0,6]]
realarray_cols = len(realarray[0])
arrayzero = [0] * realarray_cols

arrayzero[realarray[1].index(0)] = 0

for row in realarray:
    for col in row:
        if col == 0:
            arrayzero[realarray[row].index(col)] += 1



print(arrayzero)

