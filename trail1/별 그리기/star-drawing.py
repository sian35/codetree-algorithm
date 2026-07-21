N = int(input())

for i in range(N-1,-1,-1): # 1, 0
    for _ in range(i):
        print(' ', end='')
    for _ in range(2*N-1-2*i):
        print('*', end='')
    print()
for i in range(1, N): # 1
    for _ in range(i):
        print(' ', end='')
    for _ in range(2*N-1-2*i):
        print('*', end='')
    print()