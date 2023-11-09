#Does that mean like SplitThisString into Split This String?
#Or is is SplitThisString into plit his tring?
#Because for me this one is identical to 9th task
#If it is second version, check 8(second variant).py
import re

string = str(input())
emptystring = ""
split = re.findall('[A-Z][a-z]*', string)
for word in split:
    emptystring += "" + word + " "
print(emptystring)