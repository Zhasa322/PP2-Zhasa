import os

def delete(path):
        if not os.path.exists(path):
            print("The file does not exist")
            return
        if not os.access(path, os.W_OK):
            print(f"You do not have write access")
            return
        os.remove(path)

path = input("Enter path ")
delete(path)
