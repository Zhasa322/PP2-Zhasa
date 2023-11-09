import re

string = str(input())
matches = re.findall("[A-Z][a-z]+", string)
print(matches)
