word = input()

for w in word:
    if ord(w)>= ord('a') and ord(w) <= ord('z'):
        print(w.upper(), end='')
    else:
        print(w.lower(), end='')