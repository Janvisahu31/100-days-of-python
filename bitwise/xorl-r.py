def xor_till_n(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0

def xor_range(l, r):
    return xor_till_n(r) ^ xor_till_n(l - 1)

if __name__ == "__main__":
    print(xor_range(3, 9))  # Output: XOR from 3 to 9
