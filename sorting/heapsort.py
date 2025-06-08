def heapify(arr, n, i):
    """
    Helper function to maintain the heap property.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Heap Sort algorithm implementation.
    Sorts the input list in ascending order.
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == "__main__":
    sample = [12, 11, 13, 5, 6, 7]
    print("Original array:", sample)
    heap_sort(sample)
    print("Sorted array is:", sample)
