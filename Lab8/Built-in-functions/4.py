import time
import math

def squareroot(value):
    time.sleep(1.337) 
    result = math.sqrt(value)
    return result

number = float(input())
result = squareroot(number)
print("The square root of", number, "after", 1.337, "is:", result)
