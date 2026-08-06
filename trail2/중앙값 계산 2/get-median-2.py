n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(len(arr)):
    if i%2==0:
        new_arr=sorted(arr[:i+1])
        print(new_arr[len(new_arr)//2], end=' ')


