print("Welcome to the Moon mission game")
print('''
It is the year 2049. You are on a solo mission to restock the base on the moon with soil and seeds to grow more plants.
You have just landed but you are in trouble. You have landed 300 kilometers from the moon base!
You can get to the base in 3 days on your lunar rover
The lunar rover can only fit you in your spacesuit and 4 other items
Out of the items below, which do you bring? 

A: 3 litres of water
B: Shampoo
C: An extra Spacesuit
D: A shovel
E: A 10 day oxygen supply
F: Solar panels
G: The seeds for your mission
H: The soil for your mission
I: A 3 day food supply
Type the letter of the 4 items you would like to bring seperated by commas. Do not add spaces 
 Ex: A,B,C,D
''')
while True:
    choices=list(input("Enter your choice:"))
    choices.sort()
    out=list(filter(lambda x:x!=',',choices))
    correct=['A','E','F','I']
    if out==correct:
        print("Congratulations!!! You have chosen the correct choices.")
        break
    elif 'A' not in choices:
        print("Without a litre of water a day you will dehydrate.Try Again.\n")
    elif 'E' not in choices:
        print("Without Oxygen you will not have any air to breathe.Try Again.\n")
    elif 'F' not in choices:
        print("Withput solar panel your lunar rover will not have enough power to make it to base.Try Again.\n")
    else:
        print("Without food you will not make it to the moon base.Try Again.\n")