N = int(input())

arr = list(map(int, input().split()))

even = []

for a in arr:
    if a %2==0:
        even.append(a)

for i in range(len(even)-1,-1,-1):
    print(even[i], end=' ')