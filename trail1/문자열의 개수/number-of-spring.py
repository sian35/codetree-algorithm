cnt=0
odd_word=[]
while True:
    word = input()
    if word == '0':
        break
    cnt+=1
    if cnt %2 == 1:
        odd_word.append(word)

print(cnt)
for a in odd_word:
    print(a)