N = int(input())
cnt=0

for _ in range(N):
    arr = list(map(int, input().split()))
    mean = sum(arr)/len(arr)
    if mean >=60:
        print("pass")
        cnt +=1
    else:
        print("fail")

print(cnt)