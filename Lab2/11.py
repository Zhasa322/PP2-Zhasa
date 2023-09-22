a = int(input())
b = int(input())
c = int(input())
d = int(input())

if((a==c+2 and b==d+1) or (a==c+2 and d==b+1)):
    print("YES")
elif((b==d+2 and a==c+1) or (b==d+2 and c==a+1)):
    print("YES")
elif((c==a+2 and b==d+1) or (c==a+2 and d==b+1)):
    print("YES")
elif((d==b+2 and a==c+1) or (d==b+2 and c==a+1)):
    print("YES")
else:
    print("NO")