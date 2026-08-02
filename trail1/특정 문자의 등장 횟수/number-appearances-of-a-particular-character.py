word = input()
cnt_ee = 0
cnt_eb = 0
for i in range(len(word)-1):
    if word[i]+ word[i+1] == 'ee':
        cnt_ee +=1
    if word[i]+ word[i+1] == 'eb':
        cnt_eb +=1

print(cnt_ee, cnt_eb)