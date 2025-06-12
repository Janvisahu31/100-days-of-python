def find_unique(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

if __name__ == "__main__":
    print(find_unique([2, 3, 5, 4, 5, 3, 4]))  # 2
