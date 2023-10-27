def squares(a,b):
    for num in range(a,b+1):
        yield num**2
a = int(input())
b = int(input())
c = squares(a,b)
for x in range(b):
    print(next(c), end = ' ')