arr=list(map(int, input().split()))

new_arr=[]

for a in arr:
    if a==0:
        break
    new_arr.append(a)

for a in new_arr:
    if a%2==1:
        print(a+3, end=' ')
    else:
        print(a//2, end=' ')