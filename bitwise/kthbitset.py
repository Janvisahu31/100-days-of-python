def is_kth_bit_set(n, k):
    return (n & (1 << k)) != 0

if __name__ == "__main__":
    print(is_kth_bit_set(5, 0))  # True (00000101, bit 0 is set)
    print(is_kth_bit_set(5, 1))  # False
