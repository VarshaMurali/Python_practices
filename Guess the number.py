import random
print ("Welcome to Guess the number challenge")
while True:
    print ("I have guessed the number..")
    comp_guess=random.randint(1,99)
    print(comp_guess)
    print ("Its your turn...")
    my_guess=int(input("Please enter your guess: "))
    if comp_guess==my_guess:
        print("Congratulations!!! you have perfectly guessed.")
        break
    elif comp_guess>my_guess:
        print("You have guessed a smaller number")
        if (comp_guess-my_guess)<5:
            print("almost near...")
        else:
            print("and it is a wild guess..")
    else:
        print("You have guesseed a larger number")
        if (my_guess-comp_guess)<5:
            print("almost near..")
        else:
            print("and it is a wild guess..")

    proceed=input("Do you want to try again? (Y/N)")
    if proceed=='N':
        break
print("Thank you for playing the game...Will see you again")