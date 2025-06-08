def binary_search_recursive(arr, target, left, right):
    """
    Binary Search (Recursive) implementation.
    Returns index of target if found, else -1.
    """
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

if __name__ == "__main__":
    sample = [2, 3, 4, 10, 40]
    print("Index of 4:", binary_search_recursive(sample, 4, 0, len(sample) - 1))
