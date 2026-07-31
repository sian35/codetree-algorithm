n = int(input())
words = []
for _ in range(n):
    words.append(input())

char = input()
cnt=0
sum=0
for word in words:
    if word[0]==char:
        cnt+=1
        sum += len(word)

print(f"{cnt} {sum/cnt:.2f}")