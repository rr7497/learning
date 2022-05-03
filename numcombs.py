mylist = [x for x in range(0,20)]
for n in mylist: print(sum([x for x in range(mylist.index(0),mylist.index(n))]))


