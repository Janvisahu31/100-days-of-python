def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    """
    Exponential Search implementation.
    Returns index of target if found, else -1.
    """
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    return binary_search(arr, target, i // 2, min(i, len(arr) - 1))

if __name__ == "__main__":
    sample = [2, 3, 4, 10, 40, 44, 56, 78, 90, 100]
    print("Index of 56:", exponential_search(sample, 56))
