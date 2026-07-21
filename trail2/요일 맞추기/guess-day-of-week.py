m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
# 시뮬레이션이란 문제에서 주어진 규칙을 코드로 그대로 옮겨 단계별로 실행하는 유형이다

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
number_days_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

st_date=0
end_date=0
for i in range(m1):
    st_date+=number_days_month[i]
st_date += d1

for i in range(m2):
    end_date+=number_days_month[i]
end_date += d2

print(days[(end_date-st_date) % 7])
