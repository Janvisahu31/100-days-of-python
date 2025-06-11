def circular_tour(petrol, distance):
    n = len(petrol)
    start = 0
    curr_petrol = 0
    deficit = 0

    for i in range(n):
        curr_petrol += petrol[i] - distance[i]
        if curr_petrol < 0:
            start = i + 1
            deficit += curr_petrol
            curr_petrol = 0

    return start if curr_petrol + deficit >= 0 else -1

if __name__ == "__main__":
    petrol = [4, 6, 7, 4]
    distance = [6, 5, 3, 5]
    print("Start index for circular tour:", circular_tour(petrol, distance))
