word, Q = input().split()
Q = int(Q)

for _ in range(Q):
    i = int(input())
    if i==1:
        word =word[1:]+word[0]
        print(word)
    elif i==2:
        word = word[-1]+word[:len(word)-1]
        print(word)
    else:
        word = word[::-1]
        print(word)