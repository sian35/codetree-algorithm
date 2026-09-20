n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def ab(arr):
    return [abs(x) for x in arr]

answer = ab(arr)

for a in answer:
    print(a, end= ' ')