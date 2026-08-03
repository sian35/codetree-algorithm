A,B = input().split()
new_A=""
new_B=""
for a in A:
    if not a.isdigit():
        break
    new_A += a


for b in B:
    if not b.isdigit():
        break
    new_B += b

print(int(new_A)+int(new_B))