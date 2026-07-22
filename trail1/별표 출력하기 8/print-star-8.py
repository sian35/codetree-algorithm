N = int(input())

for i in range(N):
    if i %2==1:
        for _ in range(i+1):
            print('*', end=' ')
    else:
        print('*', end='')
    print()
