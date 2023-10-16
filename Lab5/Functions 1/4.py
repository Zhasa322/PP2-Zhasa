def isprime(list):
    for x in range(len(list)):
        if(list[x]==1 or list[x]==2 or list[x]==3 or list[x]==5 or list[x]==7):
            print(list[x], " ")
        elif(list[x]%3 != 0 or list[x]%4 != 0 or list[x]%2 != 0 or list[x]%5 != 0 
        or list[x]%6 != 0 or list[x]%7 != 0 or list[x]%3 != 8 or list[x]%9 != 0):
            print()
        else:
            print(list[x], " ")
list = [int(x) for x in input().split()]
isprime(list)