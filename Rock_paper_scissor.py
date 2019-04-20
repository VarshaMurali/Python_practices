import random
print ("Welcome to Rock Paper and Scissor Game")
print ("Game rules are as follows\n 1.Rock over paper-->Paper wins\n 2.Rock over scissor-->Rock wins\n 3.Scissor over paper-->Scissor wins")
while True:
    print ("Please choose your option\n 1.Rock \n 2.Paper \n 3.Scissor")
    my_choice=int(input("My choice is "))
    if my_choice>3 or my_choice<1:
        print ("Please enter a valid input")
    if my_choice==1:
        print("Your choice is Rock")
    elif my_choice==2:
        print("Your choice is Paper")
    else:
        print("Your choice is Scissor")

    comp_choice=random.randint(1,3)
    while comp_choice==my_choice:
        comp_choice=random.randint(1,3)

    if comp_choice==1:
        print("Computer choice is Rock")
    elif comp_choice==2:
        print("Computer choice is Paper")
    else:
        print("Computer choice is Scissor")

    if (my_choice==1 and comp_choice==2) or (my_choice==2 and comp_choice==1):
        print("Paper Wins")
        result=2
    elif (my_choice==2 and comp_choice==3) or (my_choice==3 and comp_choice==2):
        print("Scissor Wins")
        result=3
    else:
        print("Rock Wins")   
        result=1

    if my_choice==result:
        print("Congratulations!!!")
    else:
        print("Better Luck next time")

    proceed=input("Do you want to continue the game? (Y/N)")
    if proceed=='N':
        break
print("Thanks for playing the game..Will see you later :-)")