n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
new_arr=[]
for s in str:
    for i in range(len(t)):
        if s[i] != t[i]:
            break
        if i == len(t)-1:
            new_arr.append(s)

print(sorted(new_arr)[k-1])

