def rac(heads, legs, solved):
    chickens=0
    rabbits=0
    while solved==False:
        if chickens + rabbits == 35:
            solved = True
        elif (legs%4==0 and (chickens + legs/4 ==35)):
            rabbits = legs/4
        else:
            legs=legs-2
            chickens=chickens+1
    print("Rabbits = ",  rabbits)
    print("Chickens = ",  chickens)

heads = int(input())
legs = int(input())
solved=False
rac(heads, legs, solved)