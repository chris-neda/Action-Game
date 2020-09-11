import time
import random

enemy_list = ["wicked fairie", "ugly troll", "bad pirate"]
enemy = random.choice(enemy_list)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field,")
    print_pause("filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty")
    print_pause("(but not very effective) dagger.")
    print_pause("....")


def enemy_creature(enemy):
    if enemy == "wicked fairie":
        print_pause("Eep! It's the wicked fairie!")
        print_pause("The fairie attacks you!")
    elif enemy == "bad pirate":
        print_pause("Eep! This is the pirate's house!")
        print_pause("The pirate attacks you!")
    else:
        print_pause("Eep! This is the troll's house!")
        print_pause("The troll attacks you!")


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, i didn't unterstand that!")
    return response


def creature_house(items):
    print_pause("You approach the door of the house")
    print_pause("You are about to knock when the door opens and out steps a")
    print_pause(enemy)
    enemy_creature(enemy)
    response = valid_input("Would you like (1) to fight or (2) run away",
                           "1", "2")
    if response == '1':
        if "Sword of Ogoroth" in items:
            print_pause("As the enemy moves to attack,")
            print_pause("you unlished your new sword ")
            print_pause("The Sword of Ogoroth"
                        "shines brightly in your hand")
            print_pause("as you brace yourself for the attack")
            print_pause("But the enemy takes one look at your,"
                        "shiny new toy and run away")
            print_pause("You are victorius!")
            play_again = input("Would you like to play again? (y/n)")
            if play_again == 'y':
                play_game()
            else:
                print_pause("Thanks for playing. Good bye!")
        else:
            print_pause("You feel a bit under-prepared for this,")
            print_pause(" what whith only having a tiny dagger.")
            print_pause("You did your best...")
            print_pause("but your little dagger"
                        "is no match for the troll!")
            print_pause("You have been defeated")
            play_again = input("Would you like to play again? (y/n)")
            if play_again == 'y':
                play_game()
            else:
                print_pause("Thanks for playing. Good bye!")
    if response == '2':
        print_pause("You run back to the field")
        print_pause("Luckily, you don't seem to have been followed")
        print_pause("You are back in the field.")
        play_game()
    else:
        print_pause("Invalid Input, please try again")


def cave(items):
    print_pause("You peer cautiously into the cave.")
    print_pause("It terns out to be only a very small cave.")

    if "Sword of Ogoroth" in items:
        print_pause("You've been here. The cave is empty now.")

    else:
        print_pause("Your eyes catches a glint of metal behind a rock.")
        print_pause("It's the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger,"
                    "and take the sword with you")
        items.append("Sword of Ogoroth")
    print_pause("You walk back out to the field")
    choose(items)


def choose(items):
    print_pause("Please enter 1 or 2: ")
    answer = valid_input("Enter 1 to knock on the door of the house \n "
                         "Enter 2 to to peer into the cave",
                         "1", "2")
    if answer == '1':
        creature_house(items)
    elif answer == '2':
        cave(items)


def play_game():
    items = []
    intro()
    choose(items)


play_game()
