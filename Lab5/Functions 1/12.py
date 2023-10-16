def histogram(data):
    string=str()
    for x in range(len(data)):
        for i in range(data[x]):
            string=(string+"*")
        print(string)

data = [int(x) for x in input().split()]
histogram(data)