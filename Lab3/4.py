list = [int(x) for x in input().split(' ')]
for i in range(len(list)):
    if i > 0 and ((list[i]> 0 and list[i-1] > 0) or (list[i] < 0 and list[i-1] < 0)):
        print(list[i-1], list[i])
        break
