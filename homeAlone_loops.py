# HOME, ALONE
# the GAME (loop edition)

# by honeydiu

loop = 0
user_input = '> '
prompt = "[ENTER]"

# Introduction
print "Welcome Home, honey."
raw_input(prompt)
print "What would you like us to call you?"
name = raw_input(user_input)
print "Okay, %s. Please, make yourself at home." % name
raw_input(prompt)

# This is the first LOBBY loop when you first enter
while loop == 0:
    print "You are in the LOBBY."
    print "The door closes behind you and locks from the outside."
    raw_input(prompt)
    print "To your left is the KITCHEN."
    print "To your right is the DINING ROOM."
    print "Straight down is the LIVING ROOM."
    choice = raw_input(user_input)

    if choice.lower() == "open door":
        print "The door is locked. I'm so sorry."
        loop = 1
    elif choice.lower() == "go left" or choice.lower() == "kitchen":
        loop = 4
    elif choice.lower() == "go right" or choice.lower() == "dining room":
        loop = 2
    elif choice.lower() == "go straight" or choice.lower() == "living room":
        print "You are in the LIVING ROOM"
        raw_input(prompt)
        print "In the room hang lavish portraits of the dead tenants."
        print "You ask yourself, 'how did they die?'"
        raw_input(prompt)
        print "You look around and see a sparse SHELF, a robust BEAR RUG, "
        print "and a mahoghany COFFEE TABLE."
        loop = 3
    else:
        print "I don't know what that means."
        loop = 1

# This is the LOBBY loop after you first enter the house
while loop == 1:
    print "You are in the LOBBY."
    choice = raw_input(user_input)

    if choice.lower() == "open door":
        print "The door is locked. I'm so sorry."
        loop = 1
    elif choice.lower() == "go left" or choice.lower() == "kitchen":
        loop = 4
    elif choice.lower() == "go right" or choice.lower() == "dining room":
        loop = 2
    elif choice.lower() == "go straight" or choice.lower() == "living room":
        print "You are in the LIVING ROOM"
        raw_input(prompt)
        print "In the room hang lavish portraits of the dead tenants."
        print "You ask yourself, 'how did they die?'"
        raw_input(prompt)
        print "You look around and see a sparse SHELF, a robust BEAR RUG, "
        print "and a mahoghany COFFEE TABLE."
        loop = 3
    else:
        print "I don't know what that means."
        loop = 1

# This is the ending loop after obtain the key
while loop == 5:
    print "You are in the LOBBY."
    print "There is a staunch silence in the air."
    choice = raw_input(user_input)

    if choice.lower() == "open door":
        print "You've opened the front door."
        raw_input(prompt)
        print "You run into out of the house"
        raw_input(prompt)
        print "...into the woods"
        raw_input(prompt)
        print "..."
        raw_input(prompt)
        print "...never looking back."
        raw_input(prompt)
        print "THE END"
        quit()
    elif choice.lower() == "go left" or choice.lower() == "kitchen":
        loop = 4
    elif choice.lower() == "go right" or choice.lower() == "dining room":
        loop = 2
    elif choice.lower() == "go straight" or choice.lower() == "living room":
        print "You are in the LIVING ROOM"
        raw_input(prompt)
        print "In the room hang lavish portraits of the dead tenants."
        print "You ask yourself, 'how did they die?'"
        raw_input(prompt)
        print "You look around and see a sparse SHELF, a robust BEAR RUG, "
        print "and a mahoghany COFFEE TABLE."
        loop = 3
    else:
        print "I don't know what that means."
        loop = 5

# LIVING RM loop
while loop == 3:
    print "It feels lonely here..."
    choice = raw_input(user_input)

    if "shelf".lower() in choice:
        print "There is Kafka anthology on the shelf. Look inside?"
        shelf = raw_input(user_input)
        if shelf == "yes":
            print "You found a KEY!"
            raw_input(prompt)
            loop = 5
        else:
            loop = 3
    elif "bear" in choice or "rug" in choice:
        print "There is NOTHING under the rug."
        raw_input(prompt)
        loop = 3
    elif "coffee" in choice or "table" in choice:
        print "There is a copy of a newspaper from 1993."
        news = raw_input(user_input)
        if news == "read newspaper".lower():
            print "The headline reads: "
            print "'FAMILY MURDER SUICIDE IN LIGHT OF SCANDAL'"
            #print "Read on?"
            #read = raw_input(user_input)
            #if read == "yes":
            #    print open(homealone.txt).read()
            #    raw_input(prompt)
            #    loop = 3
            #else:
            loop = 3
    else:
        print "I don't know what that means."
        raw_input(prompt)
        loop = 3

while loop == 5:
    print "You are in the LOBBY."
    print "There is a staunch silence in the air."
    choice = raw_input(user_input)

    if choice.lower() == "open door":
        print "Congratulations, %s." % name
        raw_input(prompt)
        print "You've opened the front door."
        raw_input(prompt)
        print "You run out of the house..."
        raw_input(prompt)
        print "...into the woods"
        raw_input(prompt)
        print "..."
        raw_input(prompt)
        print "...never looking back."
        raw_input(prompt)
        print "THE END"
        quit()
    elif choice.lower() == "go left" or choice.lower() == "kitchen":
        loop = 4
    elif choice.lower() == "go right" or choice.lower() == "dining room":
        loop = 2
    elif choice.lower() == "go straight" or choice.lower() == "living room":
        loop = 3
    else:
        print "I don't know what that means."
        loop = 5
