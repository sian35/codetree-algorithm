arr = list(map(int, input().split()))
new_arr=[]
cnt=0
for a in arr:
    if a ==0:
        break
    if a % 2==0:
        cnt+=1
        new_arr.append(a)

print(cnt, sum(new_arr))