N, M = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
answer = 0 
while True:
    if M == 1:
        answer += A[0]
        break

    answer += A[M-1]

    if M % 2 == 1 :
        M -= 1
    else:
        M //= 2
    
    

print(answer)