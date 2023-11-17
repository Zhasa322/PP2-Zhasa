def check(tuple):
    return all(tuple)

truefalse = input()
splits = truefalse.split()
tuple = [x.lower() == 'true' for x in splits]
result = check(tuple)

if result:
    print("All elements are True.")
else:
    print("Not all elements are True.")
