arr = [1, 5, 3, 4, 5, 6, 2, 2, 1]
print(arr)
arr.sort()
highest = max(arr)
uniques = 0
duplicates = 0
length = len(arr)

#getting the duplicates to the end
for x in arr:
    loc = arr.index(x)
    if arr[loc] == arr[loc+1]:
        arr.pop(arr[loc])
        arr.append(arr[loc])


#counting uniques
for x in arr:
    if arr.count(x) == 1:
        uniques += 1
    
duplicates = length - uniques

print(arr)
print('the number of unique variables is',uniques)
print('the number of duplicates is',duplicates)

