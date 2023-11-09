import re

string = str(input())
emptystring = ""
split = re.split('[A-Z]', string)
for word in split:
    emptystring += "" + word + " "
print(emptystring)