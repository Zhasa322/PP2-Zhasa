a = int(input())
b = int(input())
c = int(input())
count = 0
if(a==b or a==c):
    count=count+1
if(a==b or b==c):
    count=count+1
if(a==c or b==c):
    count=count+1
print(count)
    