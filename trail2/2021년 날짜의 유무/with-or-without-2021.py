M, D = map(int, input().split())

# Please write your code here.
def define_true(M, D):
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if M >=1 and M<=12:
        if D <= month[M-1]:
            return True
        else:
            return False
    return False

print("Yes" if define_true(M,D) else "No")