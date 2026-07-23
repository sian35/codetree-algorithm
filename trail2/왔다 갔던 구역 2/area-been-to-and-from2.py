n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
arr = [0 for _ in range(2001)]
curr=0
OFFSET=1000

for j in range(n):
    if dir[j] == 'L':
        for i in range(curr - x[j], curr):
            arr[i+OFFSET] += 1
        curr -= x[j]
    elif dir[j] == 'R':
        for i in range(curr, curr + x[j]):
            arr[i+OFFSET] += 1
        curr += x[j]

cnt=0
for a in arr:
    if a>=2:
        cnt+=1

print(cnt)