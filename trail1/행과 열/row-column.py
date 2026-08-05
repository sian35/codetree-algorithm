A,B = map(int, input().split())

for i in range(A):
    for j in range(B):
        print((j+1)*(i+1), end=' ')
    print()