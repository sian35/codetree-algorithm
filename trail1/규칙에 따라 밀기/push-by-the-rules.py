A = input()
command = input()

for i in range(len(command)):
    if command[i] == 'L':
        A=A[1:]+A[0]
    else:
        A=A[-1]+A[:len(A)-1]

print(A)