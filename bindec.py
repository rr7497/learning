def bintodec(bn):
    dec = 0
    bn = str(bn)
    for x in range(-(len(bn)),0): #gets indices of each bit in bn
        if int(bn[x]) == 1: dec += 2**(abs(x+1)) #2^x where x is the index of the bit
    print(dec)
    return dec

def dectobin(dec):
    bn = 0
    count = 0
    while dec != 0: #quotient won't be 0 until the last bit
        r = dec % 2 #remainder is either 1 or 0 - these are the binary digits
        bn += r * (10**count) #add 1 or 0 in its position in bn
        dec = dec // 2 #update quotient to next quotient
        count += 1 #position in bn increases by count factor of 10
    print(bn)
    return bn

bintodec(1000101) #gives 69
dectobin(69) #gives 1000101

