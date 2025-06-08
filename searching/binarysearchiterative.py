def binary_search_iterative(arr, target):
    """
    Binary Search (Iterative) implementation.
    Returns index of target if found, else -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    sample = [2, 3, 4, 10, 40]
    print("Index of 10:", binary_search_iterative(sample, 10))
