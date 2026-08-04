A=input()
B=input()

cnt=0
result = 0
for i in range(len(A)):
    cnt+=1
    A = A[-1]+A[:len(A)-1]
    if A == B:
        result = 1
        break
        
if result == 0:
    print(-1)
else:
    print(cnt)