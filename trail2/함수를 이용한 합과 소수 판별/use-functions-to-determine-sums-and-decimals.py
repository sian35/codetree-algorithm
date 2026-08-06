a, b = map(int, input().split())

# Please write your code here.
def is_prime(n):
    for i in range(2,n//2+1):
        if n%i ==0:
            return False
    
    return True

def even_sum(n):
    return (n%10 + n //10) %2 == 0

cnt=0
for i in range(a,b+1):
    if is_prime(i) and even_sum(i):
        cnt+=1

print(cnt)