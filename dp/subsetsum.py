def subset_sum(arr, sum_value):
    n = len(arr)
    dp = [[False] * (sum_value + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sum_value + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    return dp[n][sum_value]

if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum_value = 9
    print(f"Is subset with sum {sum_value} possible?", subset_sum(arr, sum_value))
