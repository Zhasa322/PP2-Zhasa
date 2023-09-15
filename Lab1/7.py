a = int(input())
b = int(input())
c = int(input())
d = int(0)

if (a/2)%1 == 0.5:
    d=d+(a/2)+0.5
else:
    d=d+(a/2)
    
if (b/2)%1 == 0.5:
    d=d+(b/2)+0.5
else:
    d=d+(b/2)
    
if (c/2)%1 == 0.5:
    d=d+(c/2)+0.5
else:
    d=d+(c/2)
    
print(int(d))