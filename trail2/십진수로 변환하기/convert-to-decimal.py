binary = input()

# Please write your code here.
tot = len(binary)

decimal = 0
for i in range(tot):
    decimal += int(binary[tot-i-1])*(2**i)

print(decimal)