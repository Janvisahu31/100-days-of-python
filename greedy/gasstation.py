def can_complete_circuit(gas, cost):
    total, curr, start = 0, 0, 0
    for i in range(len(gas)):
        balance = gas[i] - cost[i]
        total += balance
        curr += balance
        if curr < 0:
            start = i + 1
            curr = 0
    return start if total >= 0 else -1

if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print("Start index:", can_complete_circuit(gas, cost))
