def min_coins(coins, amount):
    coins.sort(reverse=True)
    res = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            res.append(coin)
    return res

if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
    amount = 2753
    print("Coins used:", min_coins(coins, amount))
