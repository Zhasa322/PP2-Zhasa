a = int(input())
b = int(input())
c = int(input())

if((a*b)-a==c or ((a*b)-b==c)):
    print("YES")
elif((c < a*b) and (c%(a*b)==0 or c%a==0 or c%*b==0)):
    print("YES")
else:
    print("NO")