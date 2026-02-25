def sorted_arr(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr
nums = [3, 9, 7, 6, 4, 5, 3]
print(sorted_arr(nums))