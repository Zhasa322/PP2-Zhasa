import re

string = str(input())
split = re.findall('[A-Z][a-z]*', string)
snakestring = ""
counter=0
for word in split:
    if(counter>0):
        snakestring +=  "_"
    snakestring +=  word.lower()
    counter+=1
print(snakestring)