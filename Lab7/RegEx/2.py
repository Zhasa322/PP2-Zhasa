import re

string = str(input())
if re.search("ab{2,3}(?![b])", string):
    print("There is an 'a' followed by exactly two or three 'b's")
else:
    print("There is no 'a' followed by exactly two or three 'b's")
