def shell_sort(arr):
    """
    Shell Sort algorithm implementation.
    Sorts the input list in ascending order.
    """
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

if __name__ == "__main__":
    sample = [12, 34, 54, 2, 3]
    print("Original array:", sample)
    shell_sort(sample)
    print("Sorted array is:", sample)
