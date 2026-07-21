N = int(input())

for i in range(N):
    for _ in range(N-i,0,-1):
        print('*', end='')
    for _ in range(i*2):
        print(' ', end='')
    for _ in range(N-i,0,-1):
        print('*', end='')
    print()