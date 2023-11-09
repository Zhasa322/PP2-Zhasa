import re

string = str(input())
emptystring = ""
split = re.findall('[A-Z][a-z]*', string)
for word in split:
    emptystring += "" + word + " "
print(emptystring)