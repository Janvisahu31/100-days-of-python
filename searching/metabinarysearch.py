def meta_binary_search(arr, target):
    """
    Meta Binary Search implementation.
    Returns index of target if found, else -1.
    """
    n = len(arr)
    lg = n.bit_length()
    pos = 0

    for i in reversed(range(lg)):
        if (pos + (1 << i)) < n and arr[pos + (1 << i)] <= target:
            pos += (1 << i)

    if arr[pos] == target:
        return pos
    return -1

if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Index of 5:", meta_binary_search(sample, 5))
