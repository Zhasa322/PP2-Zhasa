list = [int(x) for x in input().split(' ')]
a = 1

for i in range(len(list)):
    if list[i-1] < list[i]:
        a=a+1
print(a)









