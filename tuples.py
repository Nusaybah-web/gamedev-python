nums=(1,2,3,4,5)

print(type(nums))

print(nums[4])

for i in nums:
    print(i)


for i in range(len(nums)):
    print(nums[i])

nums2=(6,7,8,9,0)

print(nums+nums2)

print(nums,nums2)

print(nums2[1:4])

del nums

#print(nums)

nums3=list(nums2)

print(nums3)

#packing

adress=(123,"catstreet","catlane",456)

door,street,area,pin=adress

print(area)