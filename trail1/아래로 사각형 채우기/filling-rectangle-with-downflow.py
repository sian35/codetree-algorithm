N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
cnt=1
for i in range(N):
    for j in range(N):
        arr[j][i] = cnt
        cnt+=1

for row in arr:
    for r in row:
        print(r, end=' ')
    print()