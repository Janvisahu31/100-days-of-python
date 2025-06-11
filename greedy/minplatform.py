def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    i = j = platforms = max_platforms = 0

    while i < len(arrivals):
        if arrivals[i] <= departures[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return max_platforms

if __name__ == "__main__":
    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]
    print("Minimum platforms needed:", min_platforms(arrivals, departures))
