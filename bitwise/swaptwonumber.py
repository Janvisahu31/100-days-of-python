def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

if __name__ == "__main__":
    a, b = swap(3, 4)
    print(a, b)  # 4, 3
