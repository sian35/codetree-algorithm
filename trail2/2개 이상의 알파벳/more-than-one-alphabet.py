A = input()

# Please write your code here.

def alphabet(arr):
    return len(set(arr)) >= 2


if alphabet(A):
    print("Yes")
else:
    print("No")