 # I want to ask, it says to find if it has a and more than zero or more b, does that mean we can just take a?
import re

a = str(input())
if(re.search("a+b*", a)):
    print("There is an a followed by zero or more b")
else:
    print("There is no a followed by zero or more b")