def bubble_sort(arr):
    """
    Bubble Sort algorithm implementation.
    Sorts the input list in ascending order.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", sample)
    bubble_sort(sample)
    print("Sorted array is:", sample)
