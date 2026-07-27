arr = list(map(int, input().split()))

max=0
min=1000

for a in arr:
    if a <500:
        if max <= a:
            max=a
    elif a >500:
        if min >= a:
            min = a
    else:
        continue

print(max, min)