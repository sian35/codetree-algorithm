a, b = map(int, input().split())
n = input()

# Please write your code here.
decimal=0
for i in range(len(n)):
    decimal+= (a**i)*int(n[len(n)-i-1])

digits=[]
while True:
    if decimal < b:
        digits.append(decimal)
        break
    digits.append(decimal%b)
    decimal = decimal // b

for d in digits[::-1]:
    print(d, end='')