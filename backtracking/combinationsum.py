def combination_sum(candidates, target):
    res = []

    def backtrack(start, target, path):
        if target == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

    backtrack(0, target, [])
    return res

if __name__ == "__main__":
    print(combination_sum([2,3,6,7], 7))
