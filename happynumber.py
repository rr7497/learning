#a happy number is any number where the sums of the squares of its digits eventually = 1
def happy(n):
    num = [int(x) for x in str(n)]
    ntemp = n*1
    count = 1
    tested = []
    while ntemp != 1 and ntemp not in tested:
        #print('calculation',count)
        #print('number:',ntemp)
        tested.append(ntemp)
        squares = []
        for x in num:
            square = x**2
            #print(str(x)+'^2 =',square)
            squares.append(square)
        #print('squares:',squares)
        ntemp = sum(squares)
        #print('sum of squares =',ntemp)
        num = [int(x) for x in str(ntemp)]
        count += 1
    if ntemp == 1: 
        #print(n,'is a happy number')
        ishappy = True
    else: 
        #print(n,'is not a happy number')
        ishappy = False
    return ishappy

def samedigits(mylist):
    samedigs = []
    for x in mylist:
        xdigs = [n for n in str(x)]
        xdigs.sort()
        for y in mylist:
            if y != x:
                ydigs = [n for n in str(y)]
                ydigs.sort()
                if xdigs == ydigs:
                    if x not in samedigs: samedigs.append(x)
                    if y not in samedigs: samedigs.append(y)
    return samedigs

def proportionhappy(top):
    happynums, unhappynums = [],[]

    for x in range(1,top+1):
        if happy(x) == True: happynums.append(x)
        elif happy(x) == False: unhappynums.append(x)
    samedigs = len(samedigits(happynums))
    counthappy = len(happynums)
    countunhappy = len(unhappynums)
    prophappy = counthappy/top * 100
    print('from 1 to',top,'there are:')
    print(counthappy,'happy numbers')
    print(countunhappy,'unhappy numbers')
    print('proportion happy:', round(prophappy,3),'%')
    print(samedigs,'of the happy numbers have the same digits')
    print('which is',round(samedigs/counthappy*100,3),'% of the happy numbers')
    print('and',round(samedigs/top*100,3),'% of all numbers')
    print()
    return counthappy, countunhappy, prophappy, samedigs

happynumbers = []
for x in range(10001):
    if happy(x) == True: happynumbers.append(x)

print(happynumbers)