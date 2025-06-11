def letter_combinations(digits):
    if not digits:
        return []
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }
    res = []

    def backtrack(idx, path):
        if idx == len(digits):
            res.append(''.join(path))
            return
        for ch in phone[digits[idx]]:
            path.append(ch)
            backtrack(idx + 1, path)
            path.pop()

    backtrack(0, [])
    return res

if __name__ == "__main__":
    print(letter_combinations("23"))
