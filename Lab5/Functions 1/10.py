def unique(list):
    list1=[]
    for x in range(len(list)):
        if(list[x] not in list1):
            list1=(*list1, list[x])
    print(*list1)
list = [int(x) for x in input().split()]
unique(list)