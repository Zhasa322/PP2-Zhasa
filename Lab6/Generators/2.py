def evens(n):
    i=0
    while i<=n:
        if(i%2==0):
            yield(i)
            if (i<n-1):
                yield ', '
        i=i+1
n=int(input())
a=evens(n)
for x in evens(n):
    print(next(a), end = "")