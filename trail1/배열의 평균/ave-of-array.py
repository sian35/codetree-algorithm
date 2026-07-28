arr = [list(map(int, input().split())) for _ in range(2)]
row=2
col=4
total_sum=0

for i in range(row):
    print(f"{sum(arr[i])/col:.1f}", end=' ')
    total_sum += sum(arr[i])
print()
for j in range(col):
    sum=0
    for i in range(row):
        sum+=arr[i][j]
    print(f"{sum/row:.1f}", end=' ')
print()
print(f"{total_sum/(row*col):.1f}")
#print(f"{sum(sum(row) for row in arr)/(row*col):.1f}")
