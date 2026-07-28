N, M = map(int, input().split())
arr_1 = [list(map(int, input().split())) for _ in range(N)]
arr_2 = [list(map(int, input().split())) for _ in range(N)]

new = [[1 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr_1[i][j]==arr_2[i][j]:
            new[i][j]=0
for row in new:
    for r in row:
        print(r, end=' ')
    print()