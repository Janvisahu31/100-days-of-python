def selection_sort(arr):
    """
    Selection Sort algorithm implementation.
    Sorts the input list in ascending order.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
    sample = [29, 10, 14, 37, 13]
    print("Original array:", sample)
    selection_sort(sample)
    print("Sorted array is:", sample)
