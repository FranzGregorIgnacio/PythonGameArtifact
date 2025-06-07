# Franz Gregor Ignacio

# Dictionary of Rooms and Items as well as Descriptions of each of the rooms
rooms = {
    'Decrepit Entrance': {'South': 'Entrance Hall', 'descEnt': 'Kamski Tech HQ has seen better days. '
                                                               'Graffiti has overtaken the walls that haven\'t'
                                                               ' crumbled and most of the windows are missing. \n'
                                                               'The glass door lies in shards to the South.'},
    'Entrance Hall': {'North': 'Decrepit Entrance', 'West': 'Laboratory', 'East': 'Canteen', 'item': 'Hacking Device',
                      'descwitem': 'The lobby is in a sorry state as the reception desk is in pieces and'
                                   ' the wallpaper is peeling.\nA sign to the West reads \"Laboratory\" while a '
                                   'sign to the East reads \"Canteen\". \nA glowing datapad flickers on the floor. '
                                   'It looks like the Hacking Device the engineers mentioned.\nIt seems to be missing'
                                   ' some parts however. Maybe they\'re around here somewhere.',
                      'descwoitem': 'The lobby is in a sorry state as the reception desk is in pieces and'
                                    ' the wallpaper is peeling.\nA sign to the West reads \"Laboratory\" while a '
                                    'sign to the East reads \"Canteen\"'},
    'Laboratory': {'East': 'Entrance Hall', 'South': 'Supply Closet', 'item': 'Batteries',
                   'descwitem': 'The laboratory had seen better days.\nShattered test tubes and '
                                'rusted machines littered the tables and walls as sparks occasionally lit '
                                'the dark room. \nA door to the South read \"Supplies\" while a door to the East read '
                                '\"Entrance Hall\". \nAs you look around, you spot '
                                'some Batteries still in their packaging. The Hacking Device needed some batteries.',
                   'descwoitem': 'The laboratory had seen better days.\nShattered test tubes and '
                                 'rusted machines littered the tables and walls as sparks occasionally lit '
                                 'the dark room. \nA door to the South read \"Supplies\" while a door to the East read '
                                 '\"Entrance Hall\".'},
    'Supply Closet': {'North': 'Laboratory', 'item': 'Antenna',
                      'descwitem': 'It was an ordinary supply closet. The main features though was that it had been'
                                   ' nearly picked clean.\nWhether it was by vagrants or machines, you\'d never know.'
                                   ' The door to the North leads back to the Laboratory. \nIn the corner you see an'
                                   ' Antenna leaning against the wall. The Hacking Device needed a new Antenna.',
                      'descwoitem': 'It was an ordinary supply closet.\nThe main feature though was that it had been'
                                    ' nearly picked clean. \nWhether it was by vagrants or machines, you\'d never know.'
                                    ' The door to the North leads back to the Laboratory.'},
    'Canteen': {'West': 'Entrance Hall', 'South': 'Abandoned Office', 'item': 'Metal Tray',
                'descwitem': 'The tables are rusty and jagged with some on their sides or back.\nThe door to '
                             'the Entrance Hall is to the West and a door leading to what looks like an '
                             'Abandoned Office lies to the South.\nNear the '
                             'serving area, a metal tray catches the light.\nThe engineers did say you needed something'
                             ' to shiny to throw off Alphamind\'s sensors. \nMaybe that Metal Tray would do.',
                'descwoitem': 'The tables are rusty and jagged with some on their sides or back.\nThe door to '
                             'the Entrance Hall is to the West '
                             'and a door leading to what looks like an Abandoned Office lies to the South.'},
    'Abandoned Office': {'North': 'Canteen', 'West': 'Server Room', 'South': 'Meeting Room', 'item': 'Kill Code',
                         'descwitem': 'Faded papers, broken computers, leftover mugs, and trash litter the office.\n'
                                      'There is hardly anything left usable as you rummage around looking for anything '
                                      'useful.\nFinally, you see a whiteboard with the words \"KILL CODE\" on it '
                                      'followed by a series of letters and numbers.\nYou remember this code being '
                                      'on the list the engineer\'s gave.\n'
                                      'To the West, you hear metal shifting behind a metal door. It looks unlocked.\n'
                                      'To the South, you see a Meeting Room through an open door.',
                         'descwoitem': 'Faded papers, broken computers, leftover mugs, and trash litter the office.\n'
                                      'There is hardly anything left usable as you rummage around looking for anything '
                                      'useful.\n'
                                      'To the West, you hear metal shifting behind a metal door. It looks unlocked.\n'
                                      'To the South, you see a Meeting Room through an open door.'},
    'Meeting Room': {'North': 'Abandoned Office', 'West': 'Tech Center', 'item': 'Keycard',
                     'descwitem': 'The wooden table in the middle is rotten and split in half.\n'
                                  'Broken chairs are turned over on the sides and a faded Keycard rests on the fallen '
                                  'whiteboard in the back.\nIllegible files and broken cases litter the floor.\n'
                                  'To the North, the door to the Abandoned Office lies open.\n'
                                  'To the West, a door leads to someplace called the \"Tech Center\"',
                     'descwoitem': 'The wooden table in the middle is rotten and split in half.\n'
                                  'Broken chairs are turned over on the sides and a fallen whiteboard sits at the back.'
                                  '\nIllegible files and broken cases litter the floor.\n'
                                  'To the North, the door to the Abandoned Office lies open.\n'
                                  'To the West, a door leads to someplace called the \"Tech Center\"'},
    'Tech Center': {'North': 'Server Room', 'East': 'Meeting Room', 'West': 'Backup Servers', 'item': 'Access Codes',
                    'descwitem': 'The door noisily slides open as rows of computers and tinkering stations '
                                 'litter the room.\nA faded banner reads \"GRAND UNVEILING NEXT TUESDAY\". '
                                 'Faded motivational posters and numerous whiteboards litter the walls that were '
                                 'still intact. \nThe rest of them showed the foundation or pipes behind them due to '
                                 'the deterioration of the place. On one of the whiteboards, the words \"ACCESS '
                                 'CODES\" with several faded codes were written in permanent marker.\nTo the North, '
                                 'a door labeled \"SERVER ROOM\" sat with a ominous red glow coming through the cracks.'
                                 '\nTo the East was the Meeting Room you came from and to the West lies a room labeled '
                                 '\"BACKUP SERVERS\".',
                    'descwoitem': 'The door noisily slides open as rows of computers and tinkering stations '
                                 'litter the room.\nA faded banner reads \"GRAND UNVEILING NEXT TUESDAY\". '
                                 'Faded motivational posters and numerous whiteboards litter the walls that were '
                                 'still intact. \nThe rest of them showed the foundation or pipes behind them due to '
                                 'the deterioration of the place.\nTo the North, a door labeled \"SERVER ROOM\" '
                                 'sat with a ominous red glow coming through the cracks.'
                                 '\nTo the East was the Meeting Room you came from and to the West lies a room labeled '
                                 '\"BACKUP SERVERS\".'},
    'Backup Servers': {'East': 'Tech Center', 'item': 'Deltamind',
                       'descwitem': 'Lines upon lines of server racks greet you in the room.\nThere isn\'t much else in'
                                    ' the room besides the servers.\nAs you search around, you find an active server '
                                    'in the corner labelled \"DELTAMIND BACKUP\" that is currently flashing green.\n'
                                    'There is a USB port nearby that you can plug your hacking device into to upload '
                                    'Deltamind to your device for the final fight with Alphamind.',
                       'descwoitem': 'Lines upon lines of server racks greet you in the room.\nThere isn\'t much else '
                                    'in the room besides the servers.\nAs you search around, you find an active server '
                                    'in the corner labelled \"DELTAMIND BACKUP\" that is currently flashing red. '
                                    'You\'ve already uploaded Deltamind to your device.\nAll that is left is to face'
                                    'Alphamind once and for all.'},
    'Server Room': {'South': 'Tech Center', 'East': 'Abandoned Office', 'item': 'Alphamind'}
    # Item in server room does nothing, just reminder of where villain is
}


# Function Declarations
# playGame is the overall game function
def playGame():
    intro()
    mainloop()


# intro is the function that prints the title, an introduction to the game, and the valid commands
def intro():
    print("Alphamind\n"
          "You pull up to the ruins of Kamski Tech HQ, a once thriving company "
          "that built advanced androids to serve the populace. Something went wrong with their central AI.\n"
          "It went rogue, calling itself \"Alphamind\". It began to slowly infect androids, turning them against "
          "their owners. \nChaos reigned in the streets until power was cut to the HQ. Since then, the androids "
          "have fallen silent.\nYet, there seems to be something stirring in the ruins of the HQ. Worrying reports "
          "that Alphamind might not be gone. \nFormer Kamski Engineers gave us a list of 8 items to purge Alphamind"
          " from the servers.\n"
          "Dive into the ruins of Kamski Tech HQ. Find these items, and shut down Alphamind. Good luck.\n"
          "Valid Commands: go South, go North, go East, go West, or get \'item name\'\n")


# playerStatus shows the player's location, inventory, and handles the inputted commands and input validation
def mainloop():
    # Initializing variables to set starting location, inventory, and win condition flag
    inv = []
    currRoom = 'Decrepit Entrance'
    winCond = False
    # Since the server room is the final room, the loop only checks if you enter that room to keep looping
    while currRoom != 'Server Room':
        playerStats(inv, currRoom)
        command = input("Enter your move:\n").lower()
        if "go" in command:
            currRoom = handlemove(currRoom, command)
        elif "get" in command:
            handleget(inv, currRoom, command)
        # General input validation error for commands that do not have get or go
        else:
            print("Invalid move!")
    # this sets the win condition of the player has all the necessary items.
    if len(inv) == 8:
        winCond = True
    # calls the endGame function to output the ending
    endGame(winCond)


# Get command handling and input validation, only allows pick up of items once and no other random items
def handleget(inv, currRoom, command):
    if rooms[currRoom]['item'] in inv and (rooms[currRoom]['item']).lower() in command:
        print("You already have the item from here!\n")
    elif (rooms[currRoom]['item']).lower() not in command:
        print("You can't grab that!\n")
    else:
        print(f"You pick up {rooms[currRoom]['item']} and store it away for later.\n")
        inv.append(rooms[currRoom]['item'])


# Go command handling and input validation, only moves in the correct direction or outputs an error if invalid
def handlemove(currRoom, command):
    if 'north' in command and 'North' in rooms[currRoom]:
        currRoom = rooms[currRoom]['North']
    elif 'south' in command and 'South' in rooms[currRoom]:
        currRoom = rooms[currRoom]['South']
    elif 'east' in command and 'East' in rooms[currRoom]:
        currRoom = rooms[currRoom]['East']
    elif 'west' in command and 'West' in rooms[currRoom]:
        currRoom = rooms[currRoom]['West']
    else:
        print(f"You can't go that way!\n")
    return currRoom


# Outputs current room, description of room, and current inventory
def playerStats(inv, currRoom):
    if currRoom != 'Decrepit Entrance' and rooms[currRoom]['item'] not in inv:
        print(rooms[currRoom]['descwitem'])
    elif currRoom != 'Decrepit Entrance':
        print(rooms[currRoom]['descwoitem'])
    else:
        print(rooms[currRoom]['descEnt'])
    print(f"\nYou are in the {currRoom}")
    if currRoom != 'Decrepit Entrance' and rooms[currRoom]['item'] not in inv:
        print(f"You see {rooms[currRoom]['item']}")
    print(f"Inventory: {inv}")
    print("Valid Commands: go South, go North, go East, go West, or get \'item name\'")
    print('-----------------------------------')


# Determines what ending to output depending on win condition being active
def endGame(winCond):
    if winCond:
        print("You slam into the room and distract Alphamind by reflecting light into its sensors.\n"
              "While it is distracted, you plug directly into its databank and access its code using \n"
              "the Access Codes and Keycard to bypass any security on it. From there, you give Deltamind \n"
              "the Kill Codes you found earlier to force a data-wipe of Alphamind's code. \n"
              "The red light dims and the speakers screech as Deltamind wipes Alphamind from the system.\n"
              "Deltamind will monitor the Kamski servers for any attempts to resurrect Alphamind.\n"
              "However, your job is done. Get some rest. You've earned it.\n"
              "Thank you for playing!")
    else:
        print("As you rush into the Server Room, you're unprepared as Alphamind slams you against a wall with an arm.\n"
              "It grabs you and slams you into another wall, then another before finally letting you slide down the "
              "wall.\nYou can feel your consciousness fading away as an arm slithers towards you.\n"
              "Everything slowly fades to black as you are dragged from the Server Room by a mechanical arm.\n"
              "Alphamind\'s harsh, static laughter echoes around you as you are dragged deeper into the "
              "HQ. \nYou are never seen again. \nThank you for playing!")


# Main body of the game where it is run
playGame()
