a = int(input())
b = int(input())
c = int(input())
d = int(input())

if(a+b==c+d):
    print("YES")
elif(a==b and c==d):
    print("YES")
elif(a+d==c+b):
    print("YES")
else:
    print("NO")