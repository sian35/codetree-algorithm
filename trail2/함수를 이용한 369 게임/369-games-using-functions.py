a, b = map(int, input().split())

# Please write your code here.

def include(n):
    return '3' in str(n) or '6' in str(n) or '9' in str(n)

def mult3(n):
    return n%3==0

cnt=0
for i in range(a,b+1):
    if mult3(i) or include(i):
        cnt+=1

print(cnt)