def insertion_sort(arr):
    """
    Insertion Sort algorithm implementation.
    Sorts the input list in ascending order.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    sample = [12, 11, 13, 5, 6]
    print("Original array:", sample)
    insertion_sort(sample)
    print("Sorted array is:", sample)
