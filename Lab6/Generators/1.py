def generateNums(n):
    i = 1
    while i <= n:
        yield i * i
        i = i + 1

n=int(input())

a = generateNums(n)
# 1 4 9 16 25 36
# next(a)
for x in range(n):
    print(next(a))
