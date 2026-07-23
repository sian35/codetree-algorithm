pp, p = map(int, input().split())

for i in range(10):
    if i ==0:
        print(pp, end=' ')
    elif i == 1:
        print(p, end=' ')
    else:
        pp, p = p, pp*2+p
        print(p, end=' ')