N = int(input())
pp=1
p=N

while True:
    if p >100:
        print(pp, end=' ')
        print(p, end=' ')
        break
    print(pp, end=' ')
    pp, p = p, p+pp

