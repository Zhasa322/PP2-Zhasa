a = int(input())
b = int(input())
c = int(input())
d = int(input())

if(a==c and (b!=d) and ((b-d>-7) or (b-d <7))):
    print("YES")
elif(b==d and (a!=c) and ((a-c>-7) or (a-c <7))):
    print("YES")
else:
    print("NO")