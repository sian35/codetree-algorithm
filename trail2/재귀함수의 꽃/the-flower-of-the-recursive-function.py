N = int(input())

# Please write your code here.
def printsth(n):
    if n==0:
        return
    print(n, end=' ')
    printsth(n-1)
    print(n, end=' ')

printsth(N)