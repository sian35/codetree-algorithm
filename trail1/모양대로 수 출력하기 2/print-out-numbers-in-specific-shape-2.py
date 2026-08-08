N = int(input())
cnt=1
for _ in range(N):
    for _ in range(N):
        print(cnt*2, end=' ')
        cnt+=1
        if cnt*2 >=10:
            cnt=1

    print()