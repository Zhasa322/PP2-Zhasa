n = int(input())
unique = set()

for i in range(n):
    line = input().split(' ')
    unique.update(line)
print(len(unique))
