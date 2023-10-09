N,M=input().split(' ')
N,M=int(N), int(M)
set1=set()
set2=set()
set3=set()
for x in range(N):
    set1.add(int(input()))
for x in range(M):
    set2.add(int(input()))
set3=set1.intersection(set2)
print(len(set3))
print(*sorted(set3))
set3=set1.difference(set2)
print(len(set3))
print(*sorted(set3))
set3=set2.difference(set1)
print(len(set3))
print(*sorted(set3))

