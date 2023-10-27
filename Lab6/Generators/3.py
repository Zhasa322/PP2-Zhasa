def iterates(n):
    i = 0
    while (i<=n):
        if(i%3==0 and i%4==0):
            yield(i)
            if(i<n-1):
                yield ', '
        i=i+1
n = int(input())
a=iterates(n)
for x in iterates(n):
    print(next(a), end = "")