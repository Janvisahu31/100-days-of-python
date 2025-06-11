def is_palindrome(s):
    return s == s[::-1]

def partition(s):
    res = []

    def backtrack(start, path):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                backtrack(end, path + [s[start:end]])

    backtrack(0, [])
    return res

if __name__ == "__main__":
    print(partition("aab"))
