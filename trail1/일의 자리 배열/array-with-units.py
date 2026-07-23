pp,p = map(int, input().split())

for i in range(10):
    if i==0:
        print(pp, end=' ')
    elif i==1:
        print(p, end=' ')
    else:   
        pp, p = p, pp+p

        if p >=10:
            p = p%10
        print(p, end=' ')