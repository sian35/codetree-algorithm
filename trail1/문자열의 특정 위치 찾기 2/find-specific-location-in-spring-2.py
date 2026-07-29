arr1="apple"
arr2="banana"
arr3="grape"
arr4="blueberry"
arr5="orange"

arr = [arr1,arr2,arr3,arr4,arr5]

find=input()
cnt=0
for a in arr:
    if a[2]==find or a[3]==find:
        print(a)
        cnt+=1

print(cnt)