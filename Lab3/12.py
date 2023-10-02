list = [int(x) for x in input().split(' ')]
values = input().split(' ')
a = int(values[0])
b = int(values[1])
c = int
list.append(0)
for i in range(len(list)-1, a, -1):
    list[i] = list[i - 1]
list[a] = b 

for i in range(len(list)):
    print(list[i], end = " ")








