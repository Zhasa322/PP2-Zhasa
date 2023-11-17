import os

def list_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(path + '/' + d)]
    return directories

def list_files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(path + '/' + f)]
    return files

def list_all(path):
    all_items = os.listdir(path)
    return all_items

path = input("Enter the path ")

directories = list_directories(path)
print("Directories:", directories)

files = list_files(path)
print("Files:", files)

all_items = list_all(path)
print("All items:", all_items)
