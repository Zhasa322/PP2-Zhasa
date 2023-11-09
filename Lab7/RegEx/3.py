import re

string = str(input())
matches = re.findall("[a-z]+_[a-z]+", string)
print(matches)
