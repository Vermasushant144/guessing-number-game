import random
randomnumber = random.randint(1,100)
print(randomnumber)
you = None
guess = 0
while (you != randomnumber):
    you = int(input("Enter the number :"))
    guess = guess + 1
    if (you == randomnumber):
        print("It is right")
    else:
        if (you>randomnumber):
            print("you guess wroung ! Enter the smaller number")
        else:
            print("you guess wroung ! Enter the larger number")    
print(f"you guessed the number {guess} guessed")