def copy(start, finish):
    with open(start, 'r') as start_file, open(finish, 'w') as finish_file:
        content = start_file.read()
        finish_file.write(content)

start_path = input("Enter start file path ")
finish_path = input("Enter finish file path ")
copy(start_path, finish_path)
