def writer(path, list):
    with open(path, 'w') as file:
        for item in list:
            file.write(str(item) + '\n')
path = input("Enter path ")
string = input()
list=[string.split()]
writer(path, list)
path.close