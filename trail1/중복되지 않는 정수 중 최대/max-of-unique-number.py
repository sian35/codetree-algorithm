n = int(input())
arr = list(map(int, input().split()))

max = -1
for i in range(len(arr)):
    if arr.count(arr[i])>1:
        continue
    if max < arr[i]:
        max = arr[i]

print(max)