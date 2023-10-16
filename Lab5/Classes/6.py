list1 = [int(x) for x in input().split()]
print(list(filter(lambda x: (x % 2 != 0 and x % 3 != 0) or x == 3 or x == 2, list1)))