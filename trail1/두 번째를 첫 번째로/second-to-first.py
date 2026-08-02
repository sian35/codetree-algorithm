word = list(input())

c1 = word[0]
c2 = word[1]

for i in range(len(word)):
    if word[i] == c2:
        word[i] = c1

print("".join(word))