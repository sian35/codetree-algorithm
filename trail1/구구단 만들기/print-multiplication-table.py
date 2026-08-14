a,b  = map(int, input().split())

even_nums = []

for i in range(a,b+1):
    if i %2 ==0:
        even_nums.append(i)

even_nums = even_nums[::-1]

for i in range(1,10):
    for j in range(len(even_nums)):
        print(even_nums[j],'*', i , '=', even_nums[j]*i, end=' ')
        if j != len(even_nums)-1:
            print("/", end=' ')

    print()
