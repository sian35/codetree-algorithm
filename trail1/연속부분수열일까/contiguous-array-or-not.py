n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt=0
for i in range(len(a)-len(b)+1):
    if a[i] == b[0]:
        curr=i
        cnt=0
        for j in range(len(b)):
            if a[curr] == b[j]:
                curr+=1
                cnt+=1
            else:
                break
        continue

if cnt == len(b):
    print("Yes")
else:
    print("No")