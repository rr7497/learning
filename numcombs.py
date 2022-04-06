mylist = [x for x in range(0,20)]
print(mylist)

for n in mylist:
    print(sum([x for x in range(mylist.index(0),mylist.index(n))]))


