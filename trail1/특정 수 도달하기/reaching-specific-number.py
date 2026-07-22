arr = list(map(int, input().split()))
new_arr=[]

for a in arr:
    new_arr.append(a)
    if a >=250:
        new_arr.pop()
        break

print(f"{sum(new_arr)} {sum(new_arr)/len(new_arr):.1f}")