def rev(string,length,reverse):
    for x in range(length):
        reverse=(*reverse, string[length-x-1])
    print(*reverse)
string = [str(x) for x in input().split()]
length = len(string)
reverse = str()
rev(string,length,reverse)