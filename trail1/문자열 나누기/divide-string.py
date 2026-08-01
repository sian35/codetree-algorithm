n = int(input())

arr = "".join(list(input().split()))

cnt=0
word = ""
for i in range(len(arr)):
    word += arr[i]
    cnt+=1
    if cnt %5 ==0 :
        print(word)
        word=""
    
    if cnt == len(arr):
        print(word)
        break
