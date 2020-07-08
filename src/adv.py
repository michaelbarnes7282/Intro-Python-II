from room import Room
from player import Player
from item import Item
from enemy import Enemy
import sys

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

# Declare enemies

enemy = {
    'slime':  Enemy('Slime', 1, 3)
}

#Add enemies to rooms

room['foyer'].enemy.append(enemy['slime'])

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

def combat():
    while player.currentRoom.enemy:
        print('\n')
        print(f'A {player.currentRoom.enemy[0].name} stands before you!')
        print(f'The {player.currentRoom.enemy[0].name} has {player.currentRoom.enemy[0].health} hitpoints and {player.currentRoom.enemy[0].strength} strength')
        combat = input('enter a to attack, or r to run: ')
        if combat == 'a':
            player.currentRoom.enemy[0].health -= player.strength
            print(f'You hit the {player.currentRoom.enemy[0].name} for {player.strength}!')
            if player.currentRoom.enemy[0].health <= 0:
                print(f'You have defeated the {player.currentRoom.enemy[0].name}!\n')
                player.currentRoom.enemy.remove(player.currentRoom.enemy[0])
                break
            player.health -= player.currentRoom.enemy[0].strength
            print(f'The {player.currentRoom.enemy[0].name} hit you for {player.currentRoom.enemy[0].strength}!')
            if player.health <= 0:
                print('Oh no! You have died, please try again.')
                sys.exit(0)
            print(f'You have {player.health} hitpoints left.')
        if combat == 'r':
            break
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

while True:
    combat()

    print(f'You are now in the: {player.currentRoom.name}')
    print(player.currentRoom.description)

    move = input('Where would you like to go? enter n, e, s, w, or q to quit. ')
    print('\n')

    if move == 'q':
        sys.exit(0)
    elif move == 'w':
        if hasattr(player.currentRoom, 'w_to'):
            player.currentRoom = player.currentRoom.w_to
        else:
            print("You cannot go that direction, try again\n")

    elif move == 'n':
        if hasattr(player.currentRoom, 'n_to'):
            player.currentRoom = player.currentRoom.n_to
        else:
            print("You cannot go that direction, try again\n")
          
    elif move == 'e':
        if hasattr(player.currentRoom, 'e_to'):
            player.currentRoom = player.currentRoom.e_to
        else:
            print("You cannot go that direction, try again\n")
    
    elif move == 's':
        if hasattr(player.currentRoom, 's_to'):
            player.currentRoom = player.currentRoom.s_to
        else:
            print("You cannot go that direction, try again\n")

