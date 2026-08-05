N = int(input())

for i in range(N):
    for j in range(N):
        if i==0 or j==N-1 or j<i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
        