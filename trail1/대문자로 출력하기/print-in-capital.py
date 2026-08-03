word = input()
word_list=[]
for c in word:
    if c.isalpha():
        word_list.append(c)

for w in word_list:
    print(w.upper(), end='')