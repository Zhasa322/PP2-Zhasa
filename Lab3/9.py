list = [int(x) for x in input().split(' ')]
a = 0
for i in range(0, len(list), 2):
    if i != len(list)-1:
        a=list[i]
        list[i]=list[i+1]
        list[i+1]=a

for i in range(len(list)):
    print(list[i])












