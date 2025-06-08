def bucket_sort(arr):
    """
    Bucket Sort algorithm implementation.
    Sorts the input list of floating point numbers in [0,1).
    """
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        index = int(n * num)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    result = []
    for bucket in buckets:
        result.extend(bucket)

    for i in range(n):
        arr[i] = result[i]

if __name__ == "__main__":
    sample = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print("Original array:", sample)
    bucket_sort(sample)
    print("Sorted array is:", sample)
