import random as r
n = 5
low,high = 0,100
nums = []
sums = []

#generate list nums of n length, randint between low to high
for x in range(n):
    nums.append(r.randint(low,high))
for x in nums:
    if nums.count(x) > 1:
        nums[nums.index(x)] = r.randint(low,high)
nums.sort()
print(nums)

#finding all sums of any 2
'''
for x in range(sum(nums)):
    for y in nums:
        for z in range(1,int(len(nums)/2)):
            if y == nums[z]: pass
            elif y + nums[z] == x:
                print(y,'+',nums[z],'=',x)
                sums.append(x)
'''

for x in nums:
    right = len(nums) - nums.index(x)
    for y in range(1,right):
        partner = nums[y]
        thesum = x + partner
        print(x,'+',partner,'=',thesum)
        sums.append(thesum)


#removing up duplicates
sums.sort()
for x in sums:
    if sums.count(x) > 1:
        sums.pop(sums.index(x))

print(sums)
