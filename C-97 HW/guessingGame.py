import random

chances = 5
list = [1,2,3,4,5,5,6,7,8,9,10]

number = random.choice(list)

while(chances > 0):

    guess = input("Enter your guess")
    guess = int(guess)

    if(guess == number):
        print("Congrulations, that was the correct number !")
        break
    elif(guess > number):
        print("Your guess is too high")
    elif(guess < number):
        print("Your number is too low")
    chances = chances - 1
    print("You have", chances, "chances left")
    
