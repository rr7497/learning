def MBTI_Functions(mbti):
    
    judg = ['null','Ti','Te','Fi','Fe']
    perc = ['null','Ni','Ne','Si','Se']
    mbti = mbti.lower()

    if mbti[-1] == 'p':
        if mbti[0] == 'e':
            for x in perc:
                if x[0].lower() == mbti[1] and x[1] == 'e': f1 = x
            for x in judg:
                if x[0].lower() == mbti[2] and x[1] == 'i': f2 = x
        elif mbti[0] == 'i':
            for x in judg:
                if x[0].lower() == mbti[2] and x[1] == 'i': f1 = x
            for x in perc:
                if x[0].lower() == mbti[1] and x[1] == 'e': f2 = x

    elif mbti[-1] == 'j':
        if mbti[0] == 'e':
            for x in judg:
                if x[0].lower() == mbti[2] and x[1] == 'e': f1 = x
            for x in perc:
                if x[0].lower() == mbti[1] and x[1] == 'i': f2 = x
        elif mbti[0] == 'i':
            for x in perc:
                if x[0].lower() == mbti[1] and x[1] == 'i': f1 = x
            for x in judg:
                if x[0].lower() == mbti[2] and x[1] == 'e': f2 = x

    for x in range(len(judg)):
        if f1 == judg[x]: f4 = judg[-x]
        if f2 == judg[x]: f3 = judg[-x]
        if f1 == perc[x]: f4 = perc[-x]
        if f2 == perc[x]: f3 = perc[-x]
    
    functions = [f1,f2,f3,f4]

    print('   Dom: ', f1)
    print('   Aux: ', f2)
    print('   Tert:', f3)
    print('   Inf: ', f4)
    return functions

def MBTI_Type(dom, aux):
    judg = [None,'Ti','Te','Fi','Fe']
    perc = [None,'Ni','Ne','Si','Se']

    for x in range(len(perc)):
        if dom == perc[x]: inf = perc[-x]
        elif dom == judg[x]: inf = judg[-x]
        if aux == perc[x]: tert = perc[-x]
        elif aux == judg[x]: tert = judg[-x]

    ei = dom[1]

    if dom[1] == 'e':
        if dom in perc: p, pj, j = dom[0].lower(), 'p', aux[0].lower()
        elif dom in judg: j, pj, p = dom[0].lower(), 'j', aux[0].lower()

    elif dom[1] == 'i':
        if dom in perc: p, pj, j = dom[0].lower(), 'j', aux[0].lower()
        elif dom in judg: j, pj, p = dom[0].lower(), 'p', aux[0].lower()

    mbti = ei + p + j + pj
    print(mbti)
    return mbti

#MBTI_Functions('esfp')
MBTI_Type('Fi','Ne')
