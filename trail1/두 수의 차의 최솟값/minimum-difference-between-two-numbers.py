n = int(input())
arr = list(map(int, input().split()))
diff = 100
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if diff > arr[j]-arr[i]:
            diff = arr[j]-arr[i]

print(diff)