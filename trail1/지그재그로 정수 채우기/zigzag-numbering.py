n,m = map(int, input().split())
cnt=0
arr = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m):
    for j in range(n):
        if i %2==0:
            arr[j][i] = cnt
        else:
            arr[n-j-1][i] = cnt
        cnt+=1

for row in arr:
    for r in row:
        print(r, end=' ')
    print()