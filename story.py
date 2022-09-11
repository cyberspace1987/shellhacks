import random
#kieran krug 9/10/2022 has created this program

print("Look up and imagine in the outer layers of space a science vessel ship is "
      "making the rounds within and around planets. Studying the genetics of species "
      "and the culture within those species of aliens.")
print("Within this space vessel it's both science, exploration and yet there's a hidden "
      "weapon within the walls of this ship.")
print("The crew is made up of transgender individuals and queer individuals.")
print("Would you like to be apart of that adventure?")

answer = input("Yes or No  ")

if answer.lower().strip() == "yes":
    print("Success and greetings!")
elif answer.lower().strip() == "no":
    print("That's a shame")
    print("As you say your goodbyes and head back to your small space pod to travel back to "
          "earth for another assignment.")
    print("It's only been 2 hours and the feeling of warmth going back "
          "home is gone when an uncloaked ship appears and captures you.")
    print("You die at the hands of hostile aliens.")
    print("End")
    quit()

print("What is your name?")
name = input()
print("What are your pronouns?")
pronouns = input()
print()

print("Imagine" + " " + name + " " + "you're in the lab studying genetic material from prehistoric alien race")
print("Imagine the head scientist named Eric, who is a transman asks you if you want to clone the fossil gene material?")

answer_2 = input("Yes or No  ")

if answer_2.lower().strip() == "yes":
    print("You two go through with the process of extracting DNA from prehistoric alien fossils.")
    print("The technology is advanced enough to create replicas of the species.")
elif answer_2.lower().strip() == "no":
    print("You think it's a bad idea and say you're going to break.")
    print(name + " " + "takes a shuttle to the nearest coffee/restaurant station in space.")
    print(name + " " + "forgot the bio packs that help regulate the shuttle came down with a virus "
                 "and they're all shutting down. You are communication less. You are tiny dot in the middle "
                 "of blackness. ")
    print("Only time will tell if you survive being lost in space. ")
    print("End")
    quit()

print("Time passes...")
print(name + " " + "and Eric figured out the structure of DNA within the species of alien.")
print("A group of hostile aliens reveal themselves suddenly but with strategic balance.")
print("From the actions within these aliens, all they want to do is take, kill, and left things forgotten.")
print("The Black Squid has an AI weapon within its walls, just in case enemies come on board.")
print("When the aliens came on board they knocked out the bio backs and the automated systems.")
print("There'll be a random number and letter. Which of those happens on you, " + name + " " + "you'll have to go")
print()

list1 = [1,2,3,4]
print(random.choice(list1))
string = "abcz"
print(random.choice(string))

answer_3 = input("Please enter your number  ")

if answer_3.lower().strip() == "1":
    print(name + " " + "goes down the dark silent corridor.")
elif answer_3.lower().strip() == "2":
    print(name + " " + " goes down to the cargo storage area.")
elif answer_3.lower().strip() == "3":
    print(name + " " + "goes down to the lab and is met with broken glass tanks, once filled with species.")
elif answer_3.lower().strip() == "4":
    print(name + " " + "goes to the control/navigation room.")
else:
    print("You've lost your way. Maybe to Summertime Sadness.")


answer_4 = input("Enter your number to move forward quickly  ")

if answer_4.lower().strip() == "1":
    print("Do you " + " " + name + " " + "go left or right?")
elif answer_4.lower().strip() == "2":
    print("Do you " + " " + name + " " + "go behind the black cage or the gold cage?")
elif answer_4.lower().strip() == "3":
    print("Do you " + " " + name + " " + "go into dark testing room or operating room?")
elif answer_4.lower().strip() == "4":
    print("Do you " + " " + name + " " + "switch on the AI weapon or call for help?")
else:
    print("Perhaps, we should just go to Space Costco?")

answer_5 = input()
if answer_5.lower().strip() == "left":
    print(pronouns + " " + "goes left and runs into black matter which an alien comes out and attacks you.")
elif answer_5.lower().strip() == "right":
    print(pronouns + " " + "goes right. Which in turn goes into the right directions towards safety.")
elif answer_5.lower().strip() == "black cage":
    print(pronouns + " " + "goes towards the black cage. In the right direction towards safety.")
elif answer_5.lower().strip() == "gold cage":
    print(pronouns + " " + "goes towards the gold cage. The direction where the species from the lab are.")
elif answer_5.lower().strip() == "dark testing room":
    print(pronouns + " " + "goes towards the dark testing room. Where the AI weapon is watching you.")
elif answer_5.lower().strip() == "operating room":
    print(pronouns + " " + "goes towards the operating room. The direction where the back door is unlocked.")
elif answer_5.lower().strip() == "AI weapon":
    print(pronouns + " " + "goes towards the AI weapon mechanism. Unleash the most sophisticated weapon to kill.")
elif answer_5.lower().strip() == "call for help":
    print(pronouns + " " + "goes towards the mechanism to call for help.")
else:
    print(name + " " + "where are you going?")

answer_6 = input("Do you remember your letter? If so, please enter ")

if answer_6.lower().strip() == "a":
    print("Your health is at 100%")
elif answer_6.lower().strip() == "b":
    print("Your health is at 50%")
elif answer_6.lower().strip() == "c":
    print("Your health is at 20%")
elif answer_6.lower().strip() == "z":
    print("Your health is at 5%")
else:
    print("Well, you're dead")

answer_7 = input("Do you want to fast track it towards safety or destruction? ")

if answer_7.lower().strip() == "safety":
    print(pronouns + " " + "is now in the shuttle pod area.")
elif answer_7.lower().strip() == "destruction":
    print(pronouns + " " + "is now in the war room with the main switch to turn on the AI weapon")
else:
    print("Where are you going?")

answer_8 = input("Please hit your option from up above again ")
if answer_8.lower().strip() == "safety":
    print(name + " " + "is in a safety pod going towards home. To find another career as well.")
elif answer_8.lower().strip() == "destruction":
    print(name + " " + "pushed the mechanism which the AI weapon unleashed it's power. Killed the aliens. Also human(s).")
else:
    print("Where are you going?")
print()
print("There'll be another set of random markings.")
print()
print("Whatever comes out will be the outcome for the crew members.")

list1 = [5, 6, 7, 8]
print(random.choice(list1))
string = "defw"
print(random.choice(string))

answer_9 = input("Please enter your number  ")

if answer_9.lower().strip() == "5":
    print("The crew members get out safely and successfully.")
elif answer_9.lower().strip() == "6":
    print("The crew members get out safely and one crew member took a sample of a testing species.")
elif answer_9.lower().strip() == "7":
    print("The crew members get out successfully yet some have been injured.")
elif answer_9.lower().strip() == "8":
    print("The crew members are injured but doing ok.")
else:
    print("You've lost your way. Maybe to Pink Venom.")

answer_10 = input("Please enter your letter  ")

if answer_10.lower().strip() == "d":
    print("Some have found other employment opportunties after this gig.")
elif answer_10.lower().strip() == "e":
    print("Some have started therapy and are needing medical leave.")
elif answer_10.lower().strip() == "f":
    print("Some are living their best life.")
elif answer_10.lower().strip() == "w":
    print("The crew members are standing beside your bedside and have been worried for months. Section 31 is "
          "waiting for you.")
else:
    print("You've lost your way. Maybe to Pink Venom.")

print("End")
quit()







