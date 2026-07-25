arr = list(map(int, input().split()))

new_arr=[]

cnt = [0 for _ in range(9)]
for a in arr:
    if a ==0:
        break
    new_arr.append(str(a))

for n in new_arr:
    if len(n) ==2:
        i = int(n[0])-1
        cnt[i]+=1

for i,c in enumerate(cnt):
    print(i+1, '-', c)