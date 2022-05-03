def tripletzero(n=int,low=int,high=int):
    import random as r
    nums = [r.randint(low,high) for x in range(n)]
    print('nums:',nums)
    ind = range(len(nums))
    triplist = []

    for a in ind:
        for b in ind:
            if a != b:
                for c in ind:
                    if c != b and c!= a:
                        A,B,C = nums[a],nums[b],nums[c]
                        triplet = [A,B,C]
                        triplet.sort()
                        if A + B + C == 0 and triplet not in triplist:
                            triplist.append(triplet)

    print('triplets:',triplist)

tripletzero(30,-15,10)
