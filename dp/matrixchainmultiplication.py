import sys

def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < dp[i][j]:
                    dp[i][j] = q
    return dp[0][n - 1]

if __name__ == "__main__":
    p = [1, 2, 3, 4]
    print("Minimum number of multiplications:", matrix_chain_order(p))
