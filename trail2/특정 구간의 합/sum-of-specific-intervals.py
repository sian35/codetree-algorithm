n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

for query in queries:
    a_1, a_2 = query
    print(sum(arr[a_1-1: a_2]))