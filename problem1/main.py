def find_min_and_max(arr):
    if not arr:
        return None
    min_arr = arr[0]
    idx_min = 0
    max_arr = arr[0]
    idx_max = 0
    for i in range (0, len(arr)):
        if arr[i] < min_arr:
            min_arr = arr[i]
            idx_min = i
        if arr[i] > max_arr:
            max_arr = arr[i]
            idx_max = i
    return f"min: {min_arr} index: {idx_min} max: {max_arr} index: {idx_max}"


if __name__ == "__main__":
    print(find_min_and_max([5, 7, 4, -2, -1, 8]))
    # min: -2 index: 3 max: 8 index: 5
    print(find_min_and_max([2, -5, -4, 22, 7, 7]))
    # min: -5 index: 1 max: 22 index: 3
    print(find_min_and_max([4, 3, 9, 4, -21, 7]))
    # min: -21 index: 4 max: 9 index: 2
    print(find_min_and_max([-1, 5, 6, 4, 2, 18]))
    # min: -1 index: 0 max: 18 index: 5
    print(find_min_and_max([-2, 5, -7, 4, 7, -20]))
    # min: -20 index: 5 max: 7 index: 4
    
    print(find_min_and_max([]))
