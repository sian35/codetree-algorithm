arr = list(input())

while len(arr)>1:
    index = int(input())
    if len(arr) <= index:
        arr.pop(-1)
    else:
        arr.pop(index)
    print("".join(arr))

