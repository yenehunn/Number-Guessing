import random
import math
lower = int(input("Enter lower bound:-"))
upper = int(input("Enter upper bound:-"))
print(f"Well come, I am thinking of a number between {lower} and {upper}")
number = random.randint(lower, upper)
print("You have ",round(math.log(upper-lower+1,2)), "chances to guess the number!\n")  
attempet = 0
while attempet < round(math.log(upper-lower+1,2)):
    guess = int (input("Enter your number:-"))
    attempet += 1
    if number == guess:
        print(f"Geat work!!! you did it in, {attempet}, trials")
    elif number > guess:
        print("You guessed too small ")  
    elif number < guess:
        print("You guessed too high ")
if attempet >= round(math.log(upper-lower+1,2)):
    print("Your guessing is more than required trials\n")  
    print("The number is %d" %number) 
    print("Good luck for the next")
