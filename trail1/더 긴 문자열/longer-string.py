arr1, arr2 = input().split()

if len(arr1) > len(arr2):
    print(arr1, len(arr1))
elif len(arr1) < len(arr2):
    print(arr2, len(arr2))
else:
    print('same')