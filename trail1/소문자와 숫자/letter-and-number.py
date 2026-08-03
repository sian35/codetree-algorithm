arr = input()

for a in arr:
    if a.isalpha() or a.isdigit():
        print(a.lower(), end='')