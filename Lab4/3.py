list = {int (x) for x in input().split(' ')}
list2 = {int (x) for x in input().split(' ')}
a = 0;
list.intersection_update(list2)
print(*sorted(list))
