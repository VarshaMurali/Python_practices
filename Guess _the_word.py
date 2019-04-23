print ("Welcome to the \"Guess The Word\" challenge")
print ("Computer has set the word.You have 5 chances to guess the word")
word="varsha"
guesses=''
turn=6
while turn>0:
    guess=input("Enter one character:")
    guesses+=guess
    fail=0 
    for char in word:
        if char in guesses:
            print (char)
        else:
            print('-')
            fail+=1
    if fail==0:
        print("You have won")
        break
    if guess not in word:
        print("Wrong guess")
        turn-=1
if turn==0:
    print("Sorry!! Out of lives...better luck next time")
else:
    print("Thank you for playing..see you again")
    