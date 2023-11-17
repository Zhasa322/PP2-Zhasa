def generate():
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        with open(letter + ".txt", 'w') as file:
            file.write(letter)
generate()
