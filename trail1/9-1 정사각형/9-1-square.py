N = int(input())
cnt=9
for _ in range(N):
    for _ in range(N):
        print(cnt, end='')
        cnt-=1
        if cnt <=0:
            cnt=9
    print()