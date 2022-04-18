def bintodec(bn):
    dec = 0
    bn = str(bn)
    for x in range(-(len(bn)),0):
        if int(bn[x]) == 1:
            dec += 2**(abs(x+1))
    print(dec)
    return dec

def dectobin(dec):
    bn = 0
    q = dec + 0
    count = 0
    while q != 0:
        r = q % 2
        bn += r * (10**count)
        q = q // 2
        count += 1
    print(bn)
    return bn

bintodec(110100100) #gives 420
dectobin(69) #gives 1000101

