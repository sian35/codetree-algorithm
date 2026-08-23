n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    if arr[i] %2 ==0:
        arr[i]= arr[i]//2
    
for a in arr:
    print(a, end=' ')