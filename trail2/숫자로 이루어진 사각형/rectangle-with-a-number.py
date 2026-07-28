n = int(input())

def print_square(n):
    start=1
    for i in range(n):
        for j in range(n):
            print(start, end=' ')
            start+=1
            if start>=10:
                start = 1
        print()

print_square(n)