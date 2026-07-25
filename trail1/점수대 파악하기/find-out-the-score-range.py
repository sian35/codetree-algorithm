arr = list(map(int, input().split()))
cnt = [0 for _ in range(10)]
for ar in arr:
    if ar == 0:
        break
    if ar <10:
        continue
    cnt[ar//10 -1] +=1

for i,c in enumerate(cnt[::-1]):
    print(100-i*10, '-', c)