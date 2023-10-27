def evens(n):
    i=0
    res = []
    while i<=n:
        if(i%2==0):
            res.append(i)
        i=i+1
    yield res
n=int(input())
a=evens(n)
print(*next(a), sep=', ')