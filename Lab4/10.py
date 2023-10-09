n, k = input().split(' ')
n, k = int(n), int(k)

strike_days = set()

for i in range(k):
    ai, bi = input().split(' ')
    ai, bi = int(ai), int(bi)
    for j in range(ai, n + 1, bi):
        if j % 7 != 6 and j % 7 != 0:
            strike_days.add(j)

total_strikes = len(strike_days)
print(total_strikes)
