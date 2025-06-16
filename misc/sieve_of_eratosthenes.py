def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
    return [i for i, is_prime in enumerate(prime) if is_prime]

if __name__ == "__main__":
    print(sieve(50))
