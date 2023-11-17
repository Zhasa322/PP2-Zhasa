import os

def check(path):
    if os.path.exists(path):
        print("The path exists")

        if os.access(path, os.R_OK):
            print("You have read access")
        else:
            print("You do not have read access")

        if os.access(path, os.W_OK):
            print("You have write access")
        else:
            print("You do not have write access")

        if os.access(path, os.X_OK):
            print("You have execute access")
        else:
            print("You do not have execute access")
    else:
        print("The path does not exist")

path = input("Enter path ")
check(path)
