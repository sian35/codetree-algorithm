N = int(input())

for i in range(2*N):
    if i % 2==0:    # i//2+1 = 별 개수
        for _ in range(i//2 + 1):
            print('*', end=' ')
    else:
        for _ in range((2*N-i)//2 +1,0,-1):
            print('*', end=' ')
    print()

