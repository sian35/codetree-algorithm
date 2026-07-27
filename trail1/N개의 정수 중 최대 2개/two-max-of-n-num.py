n = int(input())
arr = list(map(int, input().split()))

for a in sorted(arr)[-1:-3:-1]:
    print(a, end=' ')