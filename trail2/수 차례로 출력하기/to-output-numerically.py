n = int(input())

# Please write your code here.
def printasc(n):
    if n == 0:
        return
    printasc(n-1)
    print(n, end=' ')

def printdes(n):
    if n==0:
        return
    print(n, end=' ')
    printdes(n-1)

printasc(n)
print()
printdes(n)