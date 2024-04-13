import random
import math

while True:
    lower = input("Enter lower bound:-")
    while not lower.isnumeric():
        print("Please inter integer value for lower bound")
        lower = input("Enter lower bound:-")
    lower = int(lower)
    upper = input("Enter upper bound:-")
    while not upper.isnumeric():
        print("Please inter integer value for upper bound")
        upper = input("Enter upper bound:-")
    upper = int(upper)
    while upper <= lower:
        print("upper bound is must be grater than lower bound")
        lower = input("Enter lower bound:-")
        while not lower.isnumeric():
            print("Please inter integer value for lower bound")
            lower = input("Enter lower bound:-")
        lower = int(lower)
        upper = input("Enter upper bound:-")
        while not upper.isnumeric():
            print("Please inter integer value for upper bound")
            upper = input("Enter upper bound:-")
        upper = int(upper)

    print(f"Well come, I am thinking of a number between {lower} and {upper}")
    number = random.randint(lower, upper)
    print("You have ", round(math.log(upper-lower+1, 2)),
            "chances to guess the number!\n")
    attempet = 0
    while attempet < round(math.log(upper-lower+1, 2)):
        guess = int(input("Enter your number:-"))
        attempet += 1
        if number == guess:
            print(f"Geat work!!! you did it in, {attempet}, trials")
            break
        elif number > guess:
            print("You guessed too small ")
        elif number < guess:
            print("You guessed too high ")
    if attempet >= round(math.log(upper-lower+1, 2)):
        print("Your guessing is more than required trials\n")
        print("The number is %d" % number)
        print("Good luck for the next")

