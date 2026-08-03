word = input()

l = len(word)
print(word)
for i in range(l):
    print(word[l-i-1:]+word[:l-i-1])