def v(r):
    volume=(4/3) * 3.142 * r * r * r
    print(volume)
r = float(input())
v(r)


def centigrade(farenheit):
    print((5/9)*(farenheit-32))
farenheit = int(input())
centigrade(farenheit)



def histogram(data):
    string=str()
    for x in range(len(data)):
        for i in range(data[x]):
            string=(string+"*")
        print(string)

data = [int(x) for x in input().split()]
histogram(data)