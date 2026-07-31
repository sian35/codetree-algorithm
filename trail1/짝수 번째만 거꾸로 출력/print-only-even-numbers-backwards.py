words = input()

even_words =[]

for i in range(len(words)):
    if i%2 ==1:
        even_words.append(words[i])

for word in even_words[::-1]:
    print(word, end='')