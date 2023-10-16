import random
def guess(n, found, rand, name):
    counter = 1
    while(found==False):
        n = int(input())
        if(n==rand):
            print("Good job," + name + "!  You guessed my number in " + str(counter) + "  guesses!")
            found = True
        elif(n<rand):
            print("Your guess is too low.")
            print("Take a guess.")
            counter=counter+1
        else:
            print("Your guess is too high.")
            print("Take a guess.")
            counter=counter+1



print("Hello! What is your name")
name = str(input())
print("Well, " + name + ", I am thinking of a number between 1 and 20." )
print("Take a guess")
n=int()
rand = random.randint(1,20)
found=False
guess(n, found, rand, name)