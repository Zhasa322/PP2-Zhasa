
def palindrom(word: str):
    if word == word[::-1]:
        print("palindrome")
    else:
        print("Not palindrome")
word = str(input())
palindrom(word)