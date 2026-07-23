N = int(input())

arr = list(map(int, input().split()))

new_arr=[]

for a in arr:
    if a%2==0:
        new_arr.append(a)

for n in new_arr:
    print(n, end=' ')