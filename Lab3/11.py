list = [int(x) for x in input().split(' ')]
a = int(input())
for i in range(len(list)-1):
     if i >= a:
        list[i]=list[i+1]
list[-1]=""
for i in range(len(list)):
    print(list[i], end = " ")







