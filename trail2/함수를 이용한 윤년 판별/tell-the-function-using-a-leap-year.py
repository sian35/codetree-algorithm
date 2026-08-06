y = int(input())

# Please write your code here.

def leap_year(y):
    if y%4 ==0:
        if y%100==0 and y%400 !=0:
            return False
        else:
            return True
    return False

print('true' if leap_year(y) else 'false')