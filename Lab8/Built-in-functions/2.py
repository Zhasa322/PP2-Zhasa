def calc(string):
    Upper=0
    Lower=0
    for x in string:
        if('A' <= x <= 'Z'):
            Upper=Upper+1
        elif('a' <= x <= 'z'):
            Lower=Lower+1
    return Upper, Lower


string = str(input())
upper, lower = calc(string)
print("Amount of uppercase", upper)
print("Amount of lowercase", lower)

