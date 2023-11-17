def palindrome(string):
    for x in range(len(string)//2):
        if string[x] != string[len(string)-x-1]:
            return False
    return True

string = input()
if palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
