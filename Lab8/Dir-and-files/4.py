def count(path):
    open(path, 'r')
    lines=0
    for line in path:
        lines +=1
    return lines

path = input("Enter path ")
lines = count(path)
print("File has", lines ,"lines")
