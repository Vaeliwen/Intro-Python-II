from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = 'foyer'
room['outside'].e_to = None
room['outside'].s_to = None
room['outside'].w_to = None
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['foyer'].w_to = None
room['overlook'].s_to = 'foyer'
room['overlook'].w_to = None
room['overlook'].n_to = None
room['overlook'].e_to = None
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['narrow'].e_to = None
room['narrow'].s_to = None
room['treasure'].s_to = 'narrow'
room['treasure'].w_to = None
room['treasure'].e_to = None
room['treasure'].n_to = None

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

p1 = Player('outside')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

current_room = ""

def start():
    welcome_message = "Welcome to your adventure!"
    print(welcome_message)

def room_check():
    global current_room
    for x in room:
        if x == p1.currentroom:
            current_room = room.get(x)
    print(f"{current_room.name}:")
    print(current_room.description)

def get_user_choice():
    choice = input(" north | west | south | east | quit\n")
    return choice

def compare_choice_to_options():
    global current_room
    if user_choice == "north":
        if room[p1.currentroom].n_to != None:
            p1.currentroom = room[p1.currentroom].n_to
        else:
            print("There's no exit there!")
    elif user_choice == "east":
        if room[p1.currentroom].e_to != None:
            p1.currentroom = room[p1.currentroom].e_to
        else:
            print("There's no exit there!")
    elif user_choice == "south":
        if room[p1.currentroom].s_to != None:
            p1.currentroom = room[p1.currentroom].s_to
        else:
            print("There's no exit there!")
    elif user_choice == "west":
        if room[p1.currentroom].w_to != None:
            p1.currentroom = room[p1.currentroom].w_to
        else:
            print("There's no exit there!")
    else:
        print("What was that?")

def quit_game():
    print("Thank you for playing!")


start()
room_check()

print(p1.currentroom)

user_choice = get_user_choice()

while user_choice != "quit":
    compare_choice_to_options()
    room_check()
    user_choice = get_user_choice()

quit_game()
        

