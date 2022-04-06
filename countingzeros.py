import copy
array = [[0,0,0,0],
         [3,0,2,1],
         [2,4,5,6],
         [3,0,0,5],
         [4,3,0,6]]
arraytemp = copy.deepcopy(array)
array_cols = len(array[0])
arrayzero = [0] * array_cols
arraynonzero = [0] * array_cols

for row in arraytemp:
    for col in row:
        if col == 0:
            arrayzero[row.index(0)] += 1
            row[row.index(col)] = None

print(array)
print(arraytemp)
print(arrayzero)

