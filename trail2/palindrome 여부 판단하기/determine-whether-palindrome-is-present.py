A = input()

# Please write your code here.
def palindrome(string):
    return string[::]==string[::-1]

if palindrome(A):
    print("Yes")
else:
    print("No")