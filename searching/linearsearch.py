def linear_search(arr, target):
    """
    Linear Search implementation.
    Returns index of target if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    sample = [5, 3, 8, 4, 2]
    print("Index of 4:", linear_search(sample, 4))
