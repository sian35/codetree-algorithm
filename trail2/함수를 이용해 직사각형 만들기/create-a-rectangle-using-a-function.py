n,m = map(int, input().split())

def print_nm(n, m):
    for _ in range(n):
        for _ in range(m):
            print(1, end='')
        print()

print_nm(n,m)