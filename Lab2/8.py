a = int(input())
b = int(input())
c = int(input())
d = int(input())

if((a==c+1 or c==a+1) and (b==d+1 or d==b+1)):
    print("YES")
elif(a==c and (b==d+1 or d==b+1)):
    print("YES")
elif((a==c+1 or c==a+1) and b==d):
    print("YES")
else:
    print("NO")