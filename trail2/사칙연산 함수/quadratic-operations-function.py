a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def add(a,b):
    return a+b

def subtract(a,b):
    
    return a-b

def divide(a,b):
    return int(a/b)

def multiply(a,b):
    return a*b

if o == '+':
    print(a,o,c,'=', add(a,c))
elif o == '-':
    print(a,o,c,'=', subtract(a,c))
elif o == '*':
    print(a,o,c,'=', multiply(a,c))
elif o == '/':
    print(a,o,c,'=', divide(a,c))
else:
    print('False')

