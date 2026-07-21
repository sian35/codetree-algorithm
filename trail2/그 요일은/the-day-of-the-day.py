m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

number_of_days=[0,31,29,31,30,31,30,31,31,30,31,30,31]

st_date = sum(number_of_days[:m1])+d1
end_date = sum(number_of_days[:m2])+d2

diff = end_date - st_date

end_day = days[diff%7]

cnt = diff//7
if diff%7 >= days.index(A):
   cnt+=1

print(cnt)

# comments: 어이없는 실수- number_of_days에 1월 날짜를 빼먹음