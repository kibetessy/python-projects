import random 

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"] #lists:multiple elements stored in a string
options[0]

while True:
    user_input = input("Enter choice or Q to quit: ").lower()
    if user_input == "q":
        break  

    #not in checks if user input is not in the list given
    if user_input not in options:
        continue #this takes place of an error message and goes back to the beginning of the loop

    random_number = random.randint(0, 2) #assigns 0 to rock, 1 to paper, 2 to scissors
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".") 

    #check if the user won based on what the computer picked.
    if user_input == "rock" and computer_pick == "scissors"
        print("Yay! You won!")
        user_wins += 1        

    elif user_input == "scissors" and computer_pick == "paper"
        print("Yay! You won!")
        user_wins += 1        

    elif user_input == "paper" and computer_pick == "rock"
        print("Yay! You won!")
        user_wins += 1

    else:
        print("Ouch, You lost!")
        computer_wins +=1  

print("You won", user_wins, "times.")
print("The computer", computer_wins, "times")
print("Goodbye")