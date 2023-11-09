import re

string = str(input())
split = re.split("_", string)
camelstring = ""
for word in split:
    camelstring += "" + word.capitalize()
print(camelstring)
    
