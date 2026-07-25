A, B = map(int, input().split())
cnt = [0 for _ in range(10)]
while A >1:
    cnt[A%B]+=1
    A = A//B

sum=0
for c in cnt:
    sum += c**2

print(sum)