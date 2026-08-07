Y, M, D = map(int, input().split())

# Please write your code here.
def day(Y,M,D):
    if Y%4 ==0:
        lunar=True
        if Y%100 ==0:
            lunar=False
            if Y%400 ==0:
                lunar=True
    else:
        lunar=False

    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    months_lunar=[31,29,31,30,31,30,31,31,30,31,30,31]

    if lunar:
        if D <= months_lunar[M-1]:
            return True
        else:
            return False
    else:
        if D<= months[M-1]:
            return True
        else:
            return False
def season(M):
    if M>=3 and M<=5:
        return "Spring"
    elif M>=6 and M<=8:
        return "Summer"
    elif M>=9 and M<=11:
        return "Fall"
    else:
        return "Winter"

if day(Y,M,D):
    print(season(M))
else:
    print(-1)
    