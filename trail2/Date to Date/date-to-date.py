m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
month = m1
day = d1

days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
elapsed_day = 0

while True:
    if month == m2 and day == d2:
        elapsed_day+=1
        break
    elapsed_day+=1
    day+=1

    if day > days[month]:
        day=1
        month+=1

print(elapsed_day)