dice = [0 for _ in range(6)]
arr = list(map(int, input().split()))
for a in arr:
    dice[a-1]+=1

for i,d in enumerate(dice):
    print(i+1, '-', d)