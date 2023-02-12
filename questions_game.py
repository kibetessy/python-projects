name = input("Enter your name: ")
print("Welcome", name, "to our computer question game!")

#print ("Welcome" + Name + "to my computer quiz game")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit() #terminates the statement

print("Okay! Let's go! :)")
score = 0 #keep track of how many questions they have  

#.lower() for lowercases can also be added as below and converts users inputs despite the input case to lowercase
answer = input("What does GPU stand for? ")
if answer.lower() == "Graphics Processing Unit": 
    print('Correct!')
    score += 1 #increment score when user gets correct
else:
    print('Incorrect! Try Again')

answer = input("What does RAM stand for? ") #.lower() can be added at the end of input 
if answer.lower() == "Random Access Memory": 
    print('Correct!')
    score += 1
else:
    print('Incorrect! Try Again')

answer = input("What does CPU stand for? ")
if answer.lower() == "Central Processing Unit": 
    print('Correct!')
    score += 1
else:
    print('Incorrect! Try Again')

answer = input("What does ROM stand for? ")
if answer.lower() == "Read Only Memory": 
    print('Correct!')
    score += 1
else:
    print('Incorrect! Try Again')

print("You have got"  + str(score) + " questions correct!") #change  score to string 
print("You have got" + str((score / 4) * 100) + " questions correct!") #change  score to string 


