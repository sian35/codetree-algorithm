n = int(input())

arr = list(map(int, input().split()))

buy = arr[0]
profit =0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[j] > arr[i] and profit < (arr[j]-arr[i]):
            profit = arr[j]-arr[i]

print(profit)