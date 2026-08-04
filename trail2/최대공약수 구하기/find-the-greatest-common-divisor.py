n,m = map(int, input().split())

def gcd(n,m):
    if n<m:
        n,m = m,n
    if n%m ==0:
        return m
    else:
        new = n%m
        n,m = m, new
        return gcd(n,m)

print(gcd(n,m))
    