import math

a = float(input())
b = float(input())

R = b/(2*math.sin(math.pi/a))

print(round(a*R*R/2 * math.sin(2*math.pi / a)))

