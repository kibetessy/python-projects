name = input("Enter your name: ")
print("Welcome", name, "to our safari tour across Nairobi Park")

print("Do you want to go on a safari")

answer = input( "Kindly choose your preffered tour. Private Tour or Supervised Tour")

if answer == "Private Tour":
    answer = input("You will be given a map of the park for your own adventure experience. Thankyou for visiting us enjoy your drive.")

elif answer == "Supervised Tour"
    answer = input("Kindly choose from our vast range of options, one that will suit your adventure thirst:")   

    options = ["walk", "cycle", "drive"] 

while True:
    answer = input("Enter choice or Q to quit: ").lower()
    if answer == "q":
        break  

    if answer not in options:
        continue 
   
    if options == "walk":
    answer = input('You can take a walk around the lion section of the park or go for zip-line over the park')

    if answer == 'walk':
        print("You have 15km of walking through the bamboo plantation and archive section.")
    elif answer == "zip-line"
        print("Get your adrelaline going with our 5minutes zipline ride over trees section with snakes, monkeys and birds ")
    else:
        print("Invalid Option.")

if options == "cycle":
    answer = input('You can take a bicycle or go with mini-car drive through the park')

    if answer == 'bicycle':
        print("You have 15km of cycling around the park to the see the cheetah, leopards and buffalos.")
    elif answer == "mini-car"
        print("Experience a bumpy ride across the crocodile and section")
    else:
        print("Invalid Option. You got Lost")

if options == "drive":
    answer = input('You can drive using private car or our tour bus')

    if answer == 'private':
        print("You have to pay for a 1hour drive around the National Park with no instuctor.")
    elif answer == "bus tour":
        print("Get a supervised tour with our experienced tour-guides around the National Park ride")
    else:
        print("Invalid Option. You got Lost")

print("Thank you", name, "for your time")