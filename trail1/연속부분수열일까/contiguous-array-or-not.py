n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#4 4 1 4
#4 3

# if b[0] in a:
#     curr = a.index(b[0])
#     cnt=0
#     while curr < len(a) and (len(a)-curr)<=len(b):
#         print(a[curr], b[0])
#         if a[curr] == b[0]:
#             cnt=0
#             for i in range(len(b)):
#                 if a[curr] != b[i]:
#                     break
#                 else:
#                     cnt+=1
#                     curr+=1
#         else:
#             curr+=1
#     if cnt == len(b):
#         print("Yes")
#     else:
#         print("No")
# else:
#     print("No")

cnt=0
for i in range(len(a)-len(b)+1):
    if a[i] == b[0]:
        curr=i
        cnt=0
        for j in range(len(b)):
            if a[curr] == b[j]:
                curr+=1
                cnt+=1
            else:
                break
        continue

if cnt == len(b):
    print("Yes")
else:
    print("No")