import re

string = str(input())
print(re.sub(r"(\s|,|\.)", ":", string))
