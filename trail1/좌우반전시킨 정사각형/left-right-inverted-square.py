N = int(input())

for i in range(N):
    for j in range(N):
        print((N-j)*(i+1), end=' ')
    print()