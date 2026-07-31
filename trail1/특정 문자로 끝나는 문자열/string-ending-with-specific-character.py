words = []
for _ in range(10):
    words.append(input())

char = input()
cnt=0
for word in words:
    if word[-1] == char:
        print(word)
        cnt+=1

if cnt == 0:
    print("None")
