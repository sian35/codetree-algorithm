n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
cnt=1
ord=1
for col in range(n-1,-1,-1):
    for row in range(n):
        if ord %2 !=0:
            arr[n-row-1][col]= cnt
        else:
            arr[row][col] = cnt
        cnt+=1
    ord+=1

# 숫자를 채우는 시작이 가장 오른쪽임을 고려하기. (짝수나 홀수번째 col이 아니라)

for row in arr:
    for r in row:
        print(r, end=' ')
    print()