n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
sum_arr = []

for i in range(len(nums)):
    sum_arr.append(nums[i]+ nums[len(nums)-i-1])

print(max(sum_arr))