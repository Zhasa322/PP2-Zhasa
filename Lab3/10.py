list = [int(x) for x in input().split(' ')]
a = list.index(max(list))
b = list.index(min(list))
list[a], list[b] = min(list), max(list)

for j in range (len(list)):
    print(list[j], end = " ")


