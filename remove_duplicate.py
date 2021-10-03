def remove_duplicate_one(arr):
    arr = list(set(arr))
    return sorted(arr)

def remove_duplicate_two(arr):
    if len(arr) == 0:
        return [], 0
    j = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[j] = arr[i]
            j += 1
    
    return arr, j


if __name__ == "__main__":
    result, item_number = remove_duplicate_two([1,1, 1, 2, 3, 4, 4])
    print(result, item_number)