A = input()
B = input()

cnt=0
for i in range(len(A)-1):# B는 항상 길이가 2
    if A[i]+A[i+1]==B:
        cnt +=1

print(cnt)