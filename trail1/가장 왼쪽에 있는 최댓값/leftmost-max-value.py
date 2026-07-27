n = int(input())
arr = list(map(int, input().split()))

curr = len(arr)-1
while curr > 0:
    curr = arr.index(max(arr))
    print(curr+1, end=' ')
    arr = arr[:curr]
