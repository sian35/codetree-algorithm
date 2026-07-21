a, b, c = map(int, input().split())

# Please write your code here.
day = a-11

st_time = 11*60+11 + 11*24*60
end_time = b*60 + c + 24*a*60

# 예외 조건 확인하기
if (end_time - st_time) <0:
    print(-1)
else:
    print(end_time-st_time)

