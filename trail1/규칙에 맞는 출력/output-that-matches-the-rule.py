n = int(input())

for i in range(n):
    for j in range(n):
        if j<=i:
            print(n-i+j, end=' ')
    print()

# i=4, j 0~4
# 1 2 3 4 5
# n-i+j
# i=3, j 0~3
# 2 3 4 5 
# 5-3