list = [int(x) for x in input().split(' ')]
a = 0
for i in range(len(list)-1):
    if i > 0  and list[i]>list[i+1] and list[i]>list[i-1]:
        a=a+1
print(a)
