n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def define_true(a,b):
    for i in range(n1-n2+1):
        for j in range(n2):
            if b[j] != a[i+j]:
                break
            if j == n2-1:
                return True
    return False

print("Yes" if define_true(a,b) else "No")