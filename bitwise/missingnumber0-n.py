def missing_number(arr):
    n = len(arr)
    total_xor = 0
    for i in range(n + 1):
        total_xor ^= i
    arr_xor = 0
    for num in arr:
        arr_xor ^= num
    return total_xor ^ arr_xor

if __name__ == "__main__":
    print(missing_number([3, 0, 1]))  # 2
