a,b = map(int, input().split())
nums=[]
for i in range(a, b+1):
    nums.append(i)

nums = nums[::-1]

for i in range(2,10, 2):
    for j in range(len(nums)):
        print(nums[j],'*',i,'=',nums[j]*i, end=' ')
        if j != len(nums)-1:
            print('/', end=' ')
    print()