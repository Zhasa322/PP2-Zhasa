import re

string = str(input())
if(re.search("a.*b$", string)):
    print("There is an 'a' followed by anything, ending in 'b'")
else:
     print("There is no 'a' followed by anything, ending in 'b'")
