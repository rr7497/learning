import random as r
import time as t
n = 9
low,high = 0,1275
nums, sums1, sums2 = [], [], []

#generate list nums of n length, randint between low to high
for x in range(n):
    nums.append(r.randint(low,high))
for x in nums:
    if nums.count(x) > 1:
        nums[nums.index(x)] = r.randint(low,high)
nums.sort()
print('numbers:',nums)
print('n=',n)

start1 = t.time()
bubble = int(len(nums)/2)

#finding all sums of any 2 BUBBLE METHOD - not as good as brute method but interesting thought experiment
print('BUBBLE METHOD:')
ncalcs1 = 0
for num1 in nums:
    for z in range(-bubble,bubble): #getting indices to bubble y with all values in nums
        num2 = nums[z]
        if num1 == num2: pass
        else: 
            thesum = num1 + num2
            ncalcs1 += 1
            if thesum not in sums1: #don't have to remove duplicates anymore
                #print(num1,'+',num2,'=',thesum)
                sums1.append(thesum)
print('number of calculations:',ncalcs1)
sums1.sort()
end1 = t.time()

#print(sums1)
print('time taken:',end1-start1)


#finding all sums of any 2 BRUTE METHOD
start2 = t.time()
print('BRUTE METHOD:')
ncalcs2 = 0
for num1 in nums:
    for y in range(nums.index(num1) + 1, len(nums)):
        num2 = nums[y]
        thesum = num1 + num2
        ncalcs2 += 1
        if thesum not in sums2: #don't have to remove duplicates anymore
            sums2.append(thesum)
            #print(num1,'+',num2,'=',thesum)
print('number of calculations:',ncalcs2)
end2 = t.time()

#print(sums2)
print('time taken:',end2-start2)

for x in sums1:
    if x not in sums2:
        print('something went wrong')
