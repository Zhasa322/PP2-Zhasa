n = int(input())
k = int(n//60)
while k>=24:
    k=k-24
else:
    print(k)
print(n%60)
