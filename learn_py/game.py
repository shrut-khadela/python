import random
randnumber = random.randint(1,100)
# print(randnumber)
userguess = None
guess = 0

while(userguess != randnumber):
    guess += 1
    userguess = int(input("enter your guess:"))

    if(userguess == randnumber):
        print("you guess it right!!")
    else:
        if(userguess>randnumber):
            print("you guess it wrong!  guess smaller number")
        else:
            print("you guess it wrong!  guess larger number")

print("***********************")
print(f"you guess it in {guess} guesses")

with open("highscore.txt","r") as f:
    highscore = f.read()

if(guess<int(highscore)):
    print("************* you broke hiscore *************")
    with open("highscore.txt","w") as f:
        f.write(str(guess)) 