mylist = ['five','twenty','fuck','strange','happy','word']
print(mylist)

letter = "f"
contains = ["e","t"]
keep = []
'''
for x in mylist:
    if x[0] != letter:
        mylist.remove(x)
'''

for x in range(len(contains)):
    pass

while len(contains) != 0:
    for x in contains:
        for y in mylist:
            if x in y:
                keep.append(y)
        contains.remove(x)



print(mylist)

