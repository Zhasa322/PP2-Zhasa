import itertools

def perm(string, length):
    size=1
    j=1
    for i in range(length):
        size=size*j
        j=j+1
    permutations = list(itertools.permutations(string))
    for x in range(size):
        print(*permutations[x])

string = str(input())
length = len(string)
perm(string, length)