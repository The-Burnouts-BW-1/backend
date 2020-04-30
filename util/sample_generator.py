# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.

import random


class Room:
    def __init__(self, id, name, description, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y

    def __repr__(self):
        if self.e_to is not None:
            return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
        return f"({self.x}, {self.y})"

    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)

    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x

        # Start from lower-left corner (0,0)
        x = -1  # (this will become 0 on the first step)
        y = 0
        room_count = 0

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west

        # While there are rooms to be created...
        while room_count < num_rooms:

            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                x += 1
            else:
                # When we hit a wall, move up one level and start back at the beginning
                y += 1
                x = 0

            # Create a room in the given direction
            room = Room(room_count, "A Generic Room",
                        "This is a generic room.", x, y)
            # Note that in Django, you'll need to save the room after you create it

            # Save the room in the World grid
            self.grid[y][x] = room

            # Connect the new room to the previous room
            # if previous_room is not None:
            #     # direction_list = ['n', 's', 'e', 'w']
            #     # previous_room.connect_rooms(room, random.choice(direction_list))
            #     previous_room.connect_rooms(room, room_direction)

            # Update iteration variables
            room_count += 1

        # randomize room connections
        # for each node in grid

            # randomly generate connections
            # connection = random.randint(1,4)

            # handle interior rooms
            # if x=range(1,8) && y=range(1,8) can connect to nodes(x+1 && x-1) && nodes(y+1 && y-1)
            if x = range(1, 8) & & y = range(1, 8):
                room.connect_rooms(room,)

            # handle left border rooms except corners
            # elif x=0 && y=range(1,8) can connect to nodes(x+1) && nodes(y+1 && y-1)

            # handle right border rooms except corners
            # elif x=9 && y=range(1,8) can connect to nodes(x-1) && nodes(y+1 && y-1)

            # handle bottom border rooms except corners
            # elif x=range(1,8) && y=0 can connect to nodes(x+1 && x-1) && node(y+1)

            # handle top border rooms except corners
            # elif x=range(1,8) && y=9 can connect to nodes(x+1 && x-1) && node(y-1)

            # handle bottom left corner
            # elif x=0 && y=0 can connect to node(x+1) && node(y+1)

            # handle bottom right corner
            # elif x=9 && y=0 can connect to node(x+1) && node(y+1)

            # handle top left corner
            # elif x=0 && y=9 can connect to node(x+1) && node(y-1)

            # handle top right corner
            # elif x=9 && y=9 can connect to node(x-1) && node(y-1)

        # get the reverse connection to complete connections

        for row in self.grid:
            for room in row:
                print('x:', room.x, ' y:', room.y)

    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid)  # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)


w = World()
num_rooms = 100
width = 10
height = 10
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(
    f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
