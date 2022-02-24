"""4) Number Guessing Game

General Information:
I want to play a game which I can guess a number. 
The computer chooses a number in the range I chose. 
So that I can try to find the correct number which was selected by computer.

Acceptance Criteria:
* Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer. 
* Your program should prompt the user for guesses if the user guesses incorrectly, it should print whether the guess is too high or too low. 
* If the user guesses correctly, the program should print total time and total number of guesses. 
* You must import some required modules or packages You can assume that the user will enter valid input."""


import random
import time

#starting = time.strftime('%X')
start = time.gmtime()
counter = 0
numberRange = int(input("Enter first number for range please: "))
numberRange2 = int(input("Enter second number for range please: "))
pc_Guessing = random.randint(numberRange, numberRange2) # sayı aralığı

while True:
    userGuessing = int(input("Please enter your guess: "))
    counter += 1
    if pc_Guessing == userGuessing:
        print("Congratulations!! You know.. ")
        finish = list(time.gmtime()) # kullanıcı ve pc tahmini eşit olduğundaki zamanı alıyor
        print(f"You finished in {finish[3]-start[3]} hour(s), {finish[4]-start[4]} minute(s), {finish[5] - start[5]} seconds and {counter} trying !!!")
        break # programın ne kadar çalıştığını tespit ediyor
    else:
        print("Sorry.. You lost.. Try again please")
        if pc_Guessing > userGuessing: # kullanıcının girdiği değere göre yönlendirme yapılıyor
            print("you must guess a larger number")
        else:
            print("you have to guess a smaller number")