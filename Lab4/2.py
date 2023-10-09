list = {int (x) for x in input().split(' ')}
list2 = {int (x) for x in input().split(' ')}
a = 0;
list.intersection_update(list2)
for i in range(len(list)):
    a=a+1
print(a)
