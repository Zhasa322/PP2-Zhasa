def gen(n):
    i=0
    for i in range(n+1):
        yield n-i

n=int(input())
a=gen(n)
for x in range(n+1):
    print(next(a), end=' ')