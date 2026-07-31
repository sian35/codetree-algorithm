n = int(input())
sum =0
cnt =0 
for _ in range(n):
    arr = input()
    sum += len(arr)
    if arr[0]=='a':
        cnt+=1

print(sum, cnt)