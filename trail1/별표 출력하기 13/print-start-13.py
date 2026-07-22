N = int(input())

for i in range(2*N):
    if i % 2==1:
        for _ in range((i+1)//2):
            print('*', end=' ')
    else:
        for _ in range(N-(i+1)//2):
            print('*', end=' ')
    print()

# 0 3
# 2 2
# 4 1

# N-(i+1)//2

# 1 1
# 3 2
# 5 3
# 7 4 : 별: (i+1)//2 