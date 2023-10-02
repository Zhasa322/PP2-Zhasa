a = input().split(' ')
b = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
for i in b:
    print(i, end=" ")
