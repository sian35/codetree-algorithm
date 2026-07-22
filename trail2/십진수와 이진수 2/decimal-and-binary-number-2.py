N = input()

# Please write your code here.

decimal =0
for i in range(len(N)):
    decimal += (2**i)*int(N[len(N)-i-1])

decimal = 17*decimal

digits=[]
while True:
    if decimal<2:
        digits.append(decimal)
        break
    digits.append(decimal%2)
    decimal = decimal // 2

for d in digits[::-1]:
    print(d,end='')