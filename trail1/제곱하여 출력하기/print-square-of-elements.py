N = int(input())
arr = list(map(int, input().split()))

for i in [a**2 for a in arr]:
    print(i, end=' ')