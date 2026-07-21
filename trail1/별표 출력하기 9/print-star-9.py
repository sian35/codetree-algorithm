N = int(input())

for i in range(N):
    for _ in range((2*N-1-2*i)//2):
        print(' ', end=' ')
    for _ in range(2*i+1):
        print('*', end=' ')
    print()