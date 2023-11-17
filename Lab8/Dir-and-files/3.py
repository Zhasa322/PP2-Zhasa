import os

def analyze_path(path):
    if os.path.exists(path):
        print("The path exists")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(filename)
        print(directory)
    else:
        print("The path does not exist")

path = input("Enter the path ")
analyze_path(path)
