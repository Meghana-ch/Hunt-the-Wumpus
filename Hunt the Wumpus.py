import random


def print_cave():
    print('''                                       ______18______
                                      /      |       \ 
                                     /      _9__      \ 
                                    /      /    \      \ 
                                   /      /      \      \ 
                                  17     8        10     19
                                  | \   / \      /  \   / |
                                  |  \ /   \    /    \ /  |
                                  |   7     1---2     11  |   
                                  |   |    /     \    |   |
                                  |   6----5     3---12   |
                                  |   |     \   /     |   |
                                  |   \       4      /    |
                                  |    \      |     /     |
                                  \     15---14---13     /
                                   \   /            \   /
                                    \ /              \ /
                                    16---------------20''')  # when input is P printing the map of cave


def directions():
    print('''Hunt the Wumpus:
            The Wumpus lives in a completely dark cave of 20 rooms. Each
            room has 3 tunnels leading to other rooms.

            Hazards:
            1. Two rooms have bottomless pits in them.  If you go there you fall and die.
            2. Two other rooms have super-bats.  If you go there, the bats grab you and
               fly you to some random room, which could be troublesome.  Then those bats go
               to a new room different from where they came from and from the other bats.
            3. The Wumpus is not bothered by the pits or bats, as he has sucker feet and
               is too heavy for bats to lift.  Usually he is asleep.  Two things wake
               him up: Anytime you shoot an arrow, or you entering his room.  The Wumpus
               will move into the lowest-numbered adjacent room anytime you shoot an arrow.
               When you move into the Wumpus' room, then he wakes and moves if he is in an 
               odd-numbered room, but stays still otherwise.  After that, if he is in your 
               room, he snaps your neck and you die!
            Moves:
            On each move you can do the following, where input can be upper or lower-case:
            1. Move into an adjacent room.  To move enter 'M' followed by a space and
               then a room number.
            2. Shoot your guided arrow through a list of up to three adjacent rooms, which
               you specify.  Your arrow ends up in the final room.
               To shoot enter 'S' followed by the number of rooms (1..3), and then the
               list of the desired number (up to 3) of adjacent room numbers, separated
               by spaces. If an arrow can't go a direction because there is no connecting
               tunnel, it ricochets and moves to the lowest-numbered adjacent room and
               continues doing this until it has traveled the designated number of rooms.
               If the arrow hits the Wumpus, you win! If the arrow hits you, you lose. You
               automatically pick up the arrow if you go through a room with the arrow in
               it.
            3. Enter 'R' to reset the person and hazard locations, useful for testing.
            4. Enter 'C' to cheat and display current board positions.
            5. Enter 'D' to display this set of instructions.
            6. Enter 'P' to print the maze room layout.
            7. Enter 'X' to exit the game. ''')  # wen input is D printing directions


cave = {1: [5, 2, 8], 2: [10, 1, 3], 3: [2, 4, 12], 4: [14, 5, 3], 5: [4, 6, 1], 6: [7, 15, 5],
        7: [8, 6, 17], 8: [1, 9, 7], 9: [18, 8, 10], 10: [2, 9, 11], 11: [10, 12, 19], 12: [13, 11, 3],
        13: [12, 14, 20], 14: [4, 13, 15], 15: [14, 16, 6], 16: [17, 15, 20], 17: [7, 16, 18], 18: [17, 19, 9],
        19: [18, 11, 20], 20: [16, 13, 19]}  # cave's dictionary


class game:

    def init(self, wumpus, pit1, pit2, bat1, bat2):
        self.wumpus = wumpus
        self.pit1 = pit1
        self.pit2 = pit2
        self.bat1 = bat1
        self.bat2 = bat2
        self.pos = [wumpus, pit1, pit2, bat1, bat2]  # list of locations of hazards
        self.player_pos = 13
        self.arrow = -1  # arrow is with player

    def randomize_initially(self):

        self.wumpus = random.randint(1, 20)  # randomising location of wumpus(0)
        if self.wumpus == 13 or self.wumpus in self.pos:
            while self.wumpus == 13 or self.wumpus in self.pos:  # position should != to player pos or hazards pos
                self.wumpus = random.randint(1, 20)  # keep randomising till any other number comes
        self.pos.append(self.wumpus)  # adding to list of location of hazards

        # randomize pit1(1)
        self.pit1 = random.randint(1, 20)
        if self.pit1 == 13 or self.pit1 in self.pos:
            while self.pit1 == 13 or self.pit1 in self.pos:
                self.pit1 = random.randint(1, 20)
        self.pos.append(self.pit1)

        # randomize pit2(2)
        self.pit2 = random.randint(1, 20)
        if self.pit2 == 13 or self.pit2 in self.pos:
            while self.pit2 == 13 or self.pit2 in self.pos:
                self.pit2 = random.randint(1, 20)
        self.pos.append(self.pit2)

        # randomize bat1(3)
        self.bat1 = random.randint(1, 20)
        if self.bat1 == 13 or self.bat1 in self.pos:
            while self.bat1 == 13 or self.bat1 in self.pos:
                self.bat1 = random.randint(1, 20)
        self.pos.append(self.bat1)

        # randomize bat2(4)
        self.bat2 = random.randint(1, 20)
        if self.bat2 == 13 or self.bat2 in self.pos:
            while self.bat2 == 13 or self.bat2 in self.pos:
                self.bat2 = random.randint(1, 20)
        self.pos.append(self.bat2)

    def cheat(self):
        print("Cheating! Game elements are in the following rooms: ")
        print('''Wumpus    Pit1   Pit2    Bat1    Bat2    Player    Arrow
  {0}        {1}       {2}      {3}       {4}       {5}        {6}'''.format(self.pos[0], self.pos[1], self.pos[2],
                                                                             self.pos[3], self.pos[4], self.player_pos,
                                                                             self.arrow))

    def reset(self):
        self.player_pos = 13
        # list of locations of hazards

        self.wumpus = random.randint(1, 20)  # randomising location of wumpus(0)
        if self.wumpus == 13 or self.wumpus in self.pos:
            while self.wumpus == 13 or self.wumpus in self.pos:  # position should != to player pos or hazards pos
                self.wumpus = random.randint(1, 20)  # keep randomising till any other number comes
        self.pos.append(self.wumpus)  # adding to list of location of hazards

        # randomize pit1(1)
        self.pit1 = random.randint(1, 20)
        if self.pit1 == 13 or self.pit1 in self.pos:
            while self.pit1 == 13 or self.pit1 in self.pos:
                self.pit1 = random.randint(1, 20)
        self.pos.append(self.pit1)

        # randomize pit2(2)
        self.pit2 = random.randint(1, 20)
        if self.pit2 == 13 or self.pit2 in self.pos:
            while self.pit2 == 13 or self.pit2 in self.pos:
                self.pit2 = random.randint(1, 20)
        self.pos.append(self.pit2)

        # randomize bat1(3)
        self.bat1 = random.randint(1, 20)
        if self.bat1 == 13 or self.bat1 in self.pos:
            while self.bat1 == 13 or self.bat1 in self.pos:
                self.bat1 = random.randint(1, 20)
        self.pos.append(self.bat1)

        # randomize bat2(4)
        self.bat2 = random.randint(1, 20)
        if self.bat2 == 13 or self.bat2 in self.pos:
            while self.bat2 == 13 or self.bat2 in self.pos:
                self.bat2 = random.randint(1, 20)
        self.pos.append(self.bat2)

    def randomize_bat1(self):  # wen player_pos == self.bat1, use this function
        self.bat1 = random.randint(1, 20)
        if self.bat1 == self.player_pos or self.bat1 in self.pos:
            while self.bat1 == self.player_pos or self.bat1 in self.pos:  # Make sure bat1 != other hazards
                self.bat1 = random.randint(1, 20)
        self.pos[3] = self.bat1  # pos[3] is position of bat1 in the list pos

    # when player_pos == self.bat2.
    def randomize_bat2(self):
        self.bat2 = random.randint(1, 20)
        if self.bat2 == self.player_pos or self.bat2 in self.pos:
            while self.bat2 == self.player_pos or self.bat2 in self.pos:  # make sure bat2 != other hazards
                self.bat2 = random.randint(1, 20)
        self.pos[4] = self.bat2  # pos[4] is position of bat2 in the list pos

    # when bats fly the player into new room, the player position is randomised
    def randomize_person(self):
        self.player_pos = random.randint(1, 20)
        if self.player_pos == self.pos[3] or self.player_pos == self.pos[4]:
            while self.player_pos == self.pos[3] or self.player_pos == self.pos[4]:
                # randomised player position can match other hazards but not bat1 or bat2
                self.player_pos = random.randint(1, 20)  # we don't have to add to list since its separately defined

    def randomize_wumpus(self):
        self.adj_move = cave.get(self.player_pos, "none")
        self.list1 = self.adj_move.split()
        self.wumpus = random.randint(self.list1)

    def again(self):
        what = input("Do u want to play again? (Y/N): ")  # wants to play again?
        if what == 'Y':
            self.reset()  # if yes, resets the game
        elif what == 'N':
            exit()  # if no, exits the game

    def deathbypos(self):
        if self.player_pos == self.pos[0]:  # checking if player_pos = wumpus location
            if (self.player_pos % 2) == 0:  # check even or odd
                print('''You briefly feel a slimy tentacled arm as your neck is snapped.
                         It is over.''')
                print("Game over")  # even kills
                self.again()
            elif (self.player_pos % 2) != 0:  # odd, the wumpus goes away.
                self.randomize_wumpus()  # change location of wumpus
                print('''You hear a slithering sound, as the Wumpus slips away.
                         Whew, that was close!''')
        if self.player_pos == self.pos[1] or self.player_pos == self.pos[2]:
            print('''Aaaaaaaaahhhhhh.... 
                        You fall into a pit and die.''')  # player falls into pit
            self.again()

    def threats(self, cave):
        self.w = ['wumpus', 'pit1', 'pit2', 'bat1', 'bat2']  # list of threat names
        self.x = cave.get(self.player_pos,
                          "none")  # referring to the values from the cave dict acc to key, i.e.,player_pos
        for rooms in self.x:  # rooms = value numbers from dict
            for locations in self.pos:  # locations = values of hazards randomised numbers
                if rooms == locations:  # checking if any common number to see if any hazards in adjacent rooms
                    self.y = self.pos.index(rooms)  # index of that matching room
                    for hazards in self.w:
                        if self.w.index(hazards) == self.y:  # matching the index number to give a strng value to threat
                            self.threat = self.w[self.w.index(hazards)]
                            if self.threat == 'bat1':
                                print("You hear a rustling.")
                            elif self.threat == 'bat2':
                                print("You hear a rustling.")
                            elif self.threat == 'pit1':
                                print("You feel a draft.")
                            elif self.threat == 'pit2':
                                print("You feel a draft.")
                            elif self.threat == 'wumpus':
                                print("You smell a stench.")  # printing warning acc to the threat detected

    def move(self, cave):
        # check if room number is below 20
        # check if the room number entered is one of the adjacent rooms.
        global nums
        validMove = False
        self.adj_rooms = cave.get(self.player_pos, "none")
        self.room_num = int(input("Enter the room number you want to enter: "))
        if 0 < self.room_num < 21:
            for nums in self.adj_rooms:
                if self.room_num == nums:
                    validMove = True
                    self.player_pos = self.room_num  # changing the player position to a new room
                    self.adj_rooms = cave.get(self.player_pos, "none")
                    if self.player_pos == self.arrow:
                        self.arrow = -1
                        print("Congratulations, you found the arrow and can once again shoot.")
                    break
            if not validMove:
                while self.room_num != nums:
                    print(" PLease enter one the adjacent numbers {0}".format(self.adj_rooms))
                    self.room_num = int(input("Enter the room number you want to enter: "))
                    self.adj_rooms = cave.get(self.player_pos, "none")
                    if 0 < self.room_num < 21:
                        for nums in self.adj_rooms:
                            if self.room_num == nums:
                                validMove = True
                                self.player_pos = self.room_num  # changing the player position to a new room
                                self.adj_rooms = cave.get(self.player_pos, "none")
                                if self.player_pos == self.arrow:
                                    self.arrow = -1
                                    print("Congratulations, you found the arrow and can once again shoot.")
                                break
        else:
            while self.room_num > 20:
                print("Invalid room number! Please enter a room number above 0 and below 21")
                self.room_num = int(input("Enter the room number you want to enter: "))
                self.adj_rooms = cave.get(self.player_pos, "none")
                if 0 < self.room_num < 21:
                    for nums in self.adj_rooms:
                        if self.room_num == nums:
                            validMove = True
                            self.player_pos = self.room_num  # changing the player position to a new room
                            self.adj_rooms = cave.get(self.player_pos, "none")
                            if self.player_pos == self.arrow:
                                self.arrow = -1
                                print("Congratulations, you found the arrow and can once again shoot.")
                    if not validMove:
                        while self.room_num != nums:
                            print(" PLease enter one the adjacent numbers {0}".format(self.adj_rooms))
                            self.room_num = int(input("Enter the room number you want to enter: "))
                            self.adj_rooms = cave.get(self.player_pos, "none")
                            if 0 < self.room_num < 21:
                                for nums in self.adj_rooms:
                                    if self.room_num == nums:
                                        validMove = True
                                        self.player_pos = self.room_num  # changing the player position to a new room
                                        self.adj_rooms = cave.get(self.player_pos, "none")
                                        if self.player_pos == self.arrow:
                                            self.arrow = -1
                                            print("Congratulations, you found the arrow and can once again shoot.")
                                        break

    def deathbyarrow(self):
        if self.arrow == self.pos[0]:
            print('''Wumpus has just been pierced by your deadly arrow!
Congratulations on your victory, you awesome hunter you.''')
            print()
            print()
            print("Exiting Program ...")
            self.again()
        elif self.arrow == self.player_pos:
            print('''You just shot yourself. 
        Maybe Darwin was right.  You're dead.''')
            print()
            print()
            print("Exiting Program ...")
            self.again()

    def deathbyricochet(self):
        if self.arrow == self.pos[0]:
            print('''Your arrow ricochet killed the Wumpus, you lucky dog!
Accidental victory, but still you win!''')
            print()
            print()
            print("Exiting Program ...")
            self.again()
        elif self.arrow == self.player_pos:
            print('''You just shot yourself, and are dying.
It didn't take long, you're dead.''')
            print()
            print()
            print("Exiting Program ...")
            self.again()

    def check_adj1(self):
        valid4 = False
        for room in self.adj_rooms:
            if self.room == room:
                valid4 = True
                self.arrow = room
                self.deathbyarrow()
        if not valid4:
            while self.room != room:
                print("Room x is not adjacent.  Arrow ricochets...")
                self.arrow = min(self.adj_rooms)  # it ricochets to the smallest adjacent room
                self.deathbyricochet()

    def check_adj2(self):
        self.adj_0 = cave.get(self.list[0], "none")  # list of adj rooms to the first room no.
        valid5 = False
        valid6 = False
        for them in self.adj_rooms:
            if self.list[0] == them:
                valid5 = True
                for caves in self.adj_0:
                    if self.list[1] == caves:
                        valid6 = True
                        self.arrow = self.list[1]
                        self.deathbyarrow()
                if not valid6:
                    print("Room x is not adjacent.  Arrow ricochets...")
                    self.arrow = min(self.adj_0)  # it ricochets to smallest room adj to 1st room mentioned
                    self.deathbyricochet()
        if not valid5:
            print("Room x is not adjacent.  Arrow ricochets...")
            self.arrow = min(self.room)
            self.deathbyricochet()

    def check_adj3(self):
        self.adj_0 = cave.get(self.list[0], "none")  # list of adj rooms to the first room no.
        self.adj_1 = cave.get(self.list[1], "none")  # list of adj rooms to the 2nd room no.
        valid1 = False
        valid2 = False
        valid3 = False
        for a in self.adj_rooms:
            if self.list[0] == a:  # checking if first room no. is adjacent to player's room no.
                valid1 = True
                for b in self.adj_0:
                    if self.list[1] == b:  # checking if 2nd room no. is adjacent to 1st room no.
                        valid2 = True
                        for c in self.adj_1:
                            if self.list[2] == c:  # checking if 3rd room is adjacent to 2nd room no.
                                valid3 = True
                                self.arrow = self.list[2]  # this means arrow is not with player
                                self.deathbyarrow()
                                break
                        if not valid3:
                            print("Room x is not adjacent.  Arrow ricochets...")
                            self.arrow = min(self.adj_1)  # it ricochets to the smallest adjacent room
                            self.deathbyricochet()
                if not valid2:
                    print("Room x is not adjacent.  Arrow ricochets...")
                    self.arrow = min(self.adj_0)
                    self.deathbyricochet()
        if not valid1:
            print("Room x is not adjacent.  Arrow ricochets...")
            self.arrow = min(self.adj_rooms)
            self.deathbyricochet()

    def shoot(self):
        self.arrow = self.player_pos
        self.room_distance = int(input("Enter the number of rooms (1..3) into which you want to shoot: "))  # 2
        if 0 > self.room_distance > 3:
            while 0 > self.room_distance > 3:
                self.room_distance = int(input("Enter the number of rooms (1..3) into which you want to shoot: "))
        counter = 0
        self.list = []
        if self.room_distance > 1:
            while counter < self.room_distance:
                self.room = int(input("Enter the room numbers you want to shoot through: "))
                counter += 1
                self.list.append(self.room)
        if self.room_distance == 1:
            self.check_adj1()
        elif self.room_distance == 2:
            self.check_adj2()
        elif self.room_distance == 3:
            self.check_adj3()


print('''Hunt the Wumpus:
            The Wumpus lives in a completely dark cave of 20 rooms. Each
            room has 3 tunnels leading to other rooms.

            Hazards:
            1. Two rooms have bottomless pits in them.  If you go there you fall and die.
            2. Two other rooms have super-bats.  If you go there, the bats grab you and
               fly you to some random room, which could be troublesome.  Then those bats go
               to a new room different from where they came from and from the other bats.
            3. The Wumpus is not bothered by the pits or bats, as he has sucker feet and
               is too heavy for bats to lift.  Usually he is asleep.  Two things wake
               him up: Anytime you shoot an arrow, or you entering his room.  The Wumpus
               will move into the lowest-numbered adjacent room anytime you shoot an arrow.
               When you move into the Wumpus' room, then he wakes and moves if he is in an 
               odd-numbered room, but stays still otherwise.  After that, if he is in your 
               room, he snaps your neck and you die!
            Moves:
            On each move you can do the following, where input can be upper or lower-case:
            1. Move into an adjacent room.  To move enter 'M' followed by a space and
               then a room number.
            2. Shoot your guided arrow through a list of up to three adjacent rooms, which
               you specify.  Your arrow ends up in the final room.
               To shoot enter 'S' followed by the number of rooms (1..3), and then the
               list of the desired number (up to 3) of adjacent room numbers, separated
               by spaces. If an arrow can't go a direction because there is no connecting
               tunnel, it ricochets and moves to the lowest-numbered adjacent room and
               continues doing this until it has traveled the designated number of rooms.
               If the arrow hits the Wumpus, you win! If the arrow hits you, you lose. You
               automatically pick up the arrow if you go through a room with the arrow in
               it.
            3. Enter 'R' to reset the person and hazard locations, useful for testing.
            4. Enter 'C' to cheat and display current board positions.
            5. Enter 'D' to display this set of instructions.
            6. Enter 'P' to print the maze room layout.
            7. Enter 'X' to exit the game.

            Good luck!''')  # initial printing of directions and rules of game
print('''                                       ______18______
                                      /      |       \ 
                                     /      _9__      \ 
                                    /      /    \      \ 
                                   /      /      \      \ 
                                  17     8        10     19
                                  | \   / \      /  \   / |
                                  |  \ /   \    /    \ /  |
                                  |   7     1---2     11  |
                                  |   |    /     \    |   |
                                  |   6----5     3---12   |
                                  |   |     \   /     |   |
                                  |   \       4      /    |
                                  |    \      |     /     |
                                  \     15---14---13     /
                                   \   /            \   /
                                    \ /              \ /
                                    16---------------20''')  # initial printing of the map

# while (game is running):
# print the threat message
# take the move from the user (First, they take a character.. if character is P or D, R, C then you just have to call the function)
# if the user enters M, then you need take the room number
# Check to see if the room number is valid
# Make the move happen, check if the player dies or gets carried by bats. If carried by bats... randomize both bats location and player location


player = game()
player.init(14, 18, 16, 4, 2)
# player.randomize_initially()
# print(player.cheat())
while 1:
    print("Hey! You are in room {0}.".format(player.player_pos), end=' '), player.threats(cave)
    print()
    # taking input from the user
    answer = input("Enter X for exit, P for map print, D for directions, R for reset, C for cheat, M for move and S"
                   " for shoot: ")
    if answer == 'P' or answer == 'p':  # print design of cave
        print_cave()
    elif answer == 'D' or answer == 'd':  # prints the rules of game
        directions()
    elif answer == 'R' or answer == 'r':  # resets the game to initial
        player.reset()  # Put it inside the class
    elif answer == 'C' or answer == 'c':  # it shows where all hazards r present
        player.cheat()
    elif answer == 'S' or answer == 's':  # allows u to shoot an arrow
        if player.arrow != -1:
            print("Sorry, you can't shoot an arrow you don't have.  Go find it.")
        else:
            player.shoot()
    elif answer == 'M' or answer == 'm':  # allows u to move to another room
        player.move(cave)
        player.deathbypos()
        if player.player_pos == player.pos[3]:  # check if in same room at bat1.
            player.randomize_person()  # bat will fly the player to random room
            player.randomize_bat1()  # bat will then fly to random room
            print('''Woah... you're flying!
                    You've just been transported by bats to room {0}'''.format(player.player_pos))
            player.deathbypos()
            # we also have to check, after the player lands in random room via bats, does that room have wumpus or pit
        if player.player_pos == player.pos[4]:  # check if in same room as bat2
            player.randomize_person()
            player.randomize_bat2()
            print('''Woah... you're flying!
                    You've just been transported by bats to room {0}'''.format(player.player_pos))
            player.deathbypos()
            # we also have to check, after the player lands in random room via bats, does that room have wumpus or pit
    elif answer == 'X' or answer == 'x':
        exit()