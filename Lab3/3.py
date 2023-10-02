list = [int(x) for x in input().split(' ')]
for i in range(len(list)):
    if i > 0 and list[i]>list[i-1]:
        print(list[i])