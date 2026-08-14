n = int(input())

for i in range(n):
    for j in range(n):
        if j <=i:
            print((i+1)*(j+1), end= ' ')

    print()