list = [int(x) for x in input().split(' ')]
a = int(input())

for i in range(len(list)):
    if a > list[i]:
        print(list.index(list[i])+1)
        break
    elif a < list[len(list)-1]:
        print(len(list)+1)
        break
    elif len(list) == 1:
        print(len(list)+1)
        break











