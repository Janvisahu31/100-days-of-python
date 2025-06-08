def ternary_search_iterative(arr, target):
    """
    Ternary Search (Iterative) implementation.
    Returns index of target if found, else -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1

if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Index of 9:", ternary_search_iterative(sample, 9))
