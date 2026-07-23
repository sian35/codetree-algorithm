n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr = [0 for _ in range(201)]

for st, end in segments:

    for i in range(st+100, end+100):
        arr[i] += 1

print(max(arr))