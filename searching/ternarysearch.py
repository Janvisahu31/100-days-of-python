def ternary_search_recursive(arr, target, left, right):
    """
    Ternary Search (Recursive) implementation.
    Returns index of target if found, else -1.
    """
    if left > right:
        return -1

    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2

    if target < arr[mid1]:
        return ternary_search_recursive(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search_recursive(arr, target, mid2 + 1, right)
    else:
        return ternary_search_recursive(arr, target, mid1 + 1, mid2 - 1)

if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Index of 6:", ternary_search_recursive(sample, 6, 0, len(sample) - 1))
