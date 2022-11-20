import random
import time

obstacle = ["vampire", "two-headed dragon", "serpent", "gorgon", "monster"]
beast = None
options = ["1", "2"]
item = []


def print_pause(message):
    print(message)
    time.sleep(1)


def intro():
    global beast
    beast = random.choice(obstacle)
    print_pause("As a war Chief, you have been assigned by the king,"
                " to go and rescue the princess from captive.\n")
    print_pause(f"Rumor has it that a {beast} is somewhere around there,"
                "to resist anyone coming to rescue the princess.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("In your hand you hold your trusty"
                "(but not every effective) dagger.\n")


def open_the_door():
    print_pause("you approch the door of the house.\n")
    print_pause(f"you are about to knock when the door"
                f" opens and out steps a {beast}.\n")
    print_pause(f"Eep! truly there's {beast} here!\n")
    print_pause(f"The {beast} attacks you!\n")
    print_pause("you feel nervous for this,"
                "because you had only a tiny dagger.\n")


def knock_the_door():
    print_pause("you approch the door of the house.\n")
    print_pause(f"you are about to knock when the door"
                f" opens and out steps a {beast}.\n")
    print_pause(f"Eep! truly there's {beast} here!\n")
    print_pause(f"The {beast} attacks you!\n")


def defend():
    if "sword" not in item:
        open_the_door()
    else:
        knock_the_door()


def cavern():
    print_pause("you peer cautiously into the cave.\n")
    print_pause("It turns out to be a very small cave.\n")
    print_pause("Your eye catches a glint of metal behind a rock.\n")
    print_pause("You have found the magical sword of the Ogoroth!\n")
    print_pause("You discard your silly old dagger"
                " and takes the sword with you.\n")
    print_pause("you walk back to the field.\n")
    item.append("sword")


def empty_cavern():
    if "sword" not in item:
        cavern()
    else:
        print_pause("you peer cautiously into cave.\n")
        print_pause("you've been here before, and have the sword."
                    " The cave is empty now.\n")


def fight():
    fight_choice = ""
    validate_input = False
    while validate_input is False:
        fight_choice = input("what would you like to do?"
                             " (1) fight or (2) Run away ?\n")
        if fight_choice.isnumeric() and fight_choice in options:
            validate_input = True
        else:
            print_pause("Enter valid input\n")

    if fight_choice == "1":
        if "sword" in item:
            print_pause(f"As the {beast} moves to attack,"
                        "you unsheath your new sword.\n")
            print_pause("The Ogoroth sword shrines brightly in your hand"
                        " as you brace yourself for the attack.\n")
            print_pause(f"But the {beast} takes a one look at"
                        " your new shiny toy and runs away!")
            print_pause("You have save the princess. You are victorius!\n")
        else:
            print_pause("You do your best...\n")
            print_pause(f"but your dagger is no match for {beast}.\n")
            print_pause("You have been defeated!")

    elif fight_choice == "2":
        print_pause("You run back to the field. Luckily,"
                    " you don't seem to have been followed.\n")
        game()


def repeat_game_again():
    optionYN = ["yes", "no"]
    validateInput = False
    while validateInput is False:
        repeat_again = input("would you like to play?"
                             " say yes or no?\n").lower()
        if repeat_again in optionYN:
            validateInput = True
        else:
            print_pause("Invalid selection!!!\n")

    if repeat_again == "yes":
        print_pause("Excellent!! Restarting the game ...")
        intro()
        game()

    else:
        print_pause("Thank you for playing. Game Over!\n")


def game():
    validateInput = False
    while validateInput is False:
        game_choice = input("Enter 1 to knock on the door of the house.\n"
                            "Enter 2 to peer into the cave.\n"
                            "what would you like to do?\n"
                            "(please enter 1 or 2?)\n")
        if game_choice.isnumeric() and game_choice in options:
            validateInput = True
        else:
            print_pause("Enter valid input\n")

    if game_choice == "1":
        defend()
        fight()
        repeat_game_again()

    elif game_choice == "2":
        empty_cavern()
        game()

    else:
        print_pause("Enter valid input.\n")
        game()


intro()
game()
