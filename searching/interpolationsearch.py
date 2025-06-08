def interpolation_search(arr, target):
    """
    Interpolation Search implementation.
    Returns index of target if found, else -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((high - low) * (target - arr[low])) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

if __name__ == "__main__":
    sample = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    print("Index of 18:", interpolation_search(sample, 18))
