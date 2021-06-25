

arr = [5, 8, 7, 4, 5, 6, 5, 9, 6, 5, 9, 8, 2, 3, 1, 2, 5, 4, 5, 2, 5, 4, 5, 65, 4, 8, 4]
brr = []
for i in arr:
    if i not in brr:
        brr.append(i)
print(brr)
arr = set(arr)
print(arr)

arr1 = [14, 5, 8, 6, 'a', 'b', 'c', 3, 4, 7]
