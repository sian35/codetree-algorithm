situation = [0 for _ in range(4)]
a_cnt = 0
for _ in range(3):
    symp, temp = input().split()
    temp = int(temp)

    if symp == 'Y' and temp >=37:
        situation[0]+=1
        a_cnt+=1
    elif symp == 'N' and temp >=37:
        situation[1]+=1
    elif symp == 'Y' and temp <37:
        situation[2]+=1
    else:
        situation[3]+=1

    
if a_cnt >=2:
    situation.append('E')

for s in situation:
    print(s, end=' ')