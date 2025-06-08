import math

def jump_search(arr, target):
    """
    Jump Search implementation.
    Returns index of target if found, else -1.
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Index of 7:", jump_search(sample, 7))
