N,Q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0]==1:
        print(arr[q[1]-1])
    elif q[0]==2:
        if q[1] in arr:
            print(arr.index(q[1])+1)
        else:
            print(0)
    else:
        for i in range(q[1]-1, q[2]):
            print(arr[i], end=' ')
        print()