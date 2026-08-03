arr1 = input()
arr2 = input()
new_a=""
new_b=""
for a in arr1:
    if a.isalpha():
        continue
    new_a +=a
for b in arr2:
    if b.isalpha():
        continue
    new_b +=b

print(int(new_a)+int(new_b))
    