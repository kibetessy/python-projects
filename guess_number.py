import random

#this generate a number from -1 to 15 but doesn't include 15. make it 16 to generate including 15
#random.randrange(15) 

#generates numbers from 0 to 15 minus 1
#random.randrange(-1, 15) 

#using randint, has a start and a stop. code below works as above but now includes the 15 or nth number
#r = random.randint(5, 15) 
#print (r)

highest_range = input('Enter a number: ')

if highest_range.isdigit():                     #make sure what the user input is a digit before converting it
    highest_range = int(highest_range)          #wrap input in int for conversion 

    if highest_range <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, highest_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Take a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time.")
        continue        #takes back to the top of the loop
    
    if user_guess ==  random_number:
        print("Good, you got it right")
        break   #stops or exits the loop
    elif user_guess > random_number: #elif makes the use of else....is statements easier to read
        print("Sorry, you are above the number!")
    else:
        print("Sorry, you are below the number!")

print("You got it in", guesses, "guesses")
    


