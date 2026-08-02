s,q = input().split()
s=list(s)
q=int(q)

for _ in range(q):
    query = list(input().split())

    if query[0] == '1':
        a, b = int(query[1]), int(query[2])
        s[a-1], s[b-1] = s[b-1], s[a-1]
        print("".join(s))
    elif query[0] == '2':
        x,y = query[1], query[2]
        for i in range(len(s)):
            if s[i] == x:
                s[i] = y
        
        print("".join(s))
