arr = input().split()

new_arr=[]
for i in range(len(arr)):
    if arr[i]=='0':
        break
    new_arr.append(arr[i])


print(" ".join(new_arr[::-1]))