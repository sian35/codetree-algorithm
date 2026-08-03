A = input()

sum=0
for a in A:
    if a.isdigit():
        sum +=int(a)

print(sum)