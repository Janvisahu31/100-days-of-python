def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    n = 10
    print(f"Fibonacci({n}) =", fibonacci(n))
