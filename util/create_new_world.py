from django.contrib.auth.models import User
from adventure.models import Player, Room
# from .sample_generator import *
import random
def generate_rooms(size_x, size_y, num_rooms):
	grid = [None] * size_y
	width = size_x
	height = size_y
	for i in range(len(grid)):
		grid[i] = [None] * size_x
	x = -1
	y = 0
	room_count = 0
	direction = 1
	while room_count < num_rooms:
		if direction > 0 and x < size_x - 1:
			x += 1
		else:
			y += 1
			x = 0
		room = Room(room_id = room_count, title = "A Generic Room", description = "This is a generic room.", x = x, y = y)
		# Save the room in the World grid
		grid[y][x] = room
		room.save()
		room_count += 1
	for row in grid:
		for room in row:
			direction_list = ['n', 's', 'e', 'w']
			new_y = room.y
			new_x = room.x
			num_loops = 0
			while num_loops <= 1:
				direction = random.choice(direction_list)
				if direction == 'n' and room.x <= 9 and room.y < 9:
					new_y = room.y + 1
					room.connect_rooms(grid[new_y][new_x], direction)
				elif direction == 's' and room.x <= 9 and room.y > 0:
					new_y = room.y - 1
					room.connect_rooms(grid[new_y][new_x], direction)
				elif direction == 'e' and room.x >= 0 and room.x < 9 and room.y >= 0 and room.y < 10:
					new_x = room.x + 1
					room.connect_rooms(grid[new_y][new_x], direction)
				elif direction == 'w' and room.x >= 1 and room.x < 10 and room.y >= 0 and room.y < 10:
					new_x = room.x - 1
					room.connect_rooms(grid[new_y][new_x], direction)	
				num_loops += 1
	return grid

generate_rooms(10, 10, 100)

players=Player.objects.all()
for p in players:
  	room_id = random.randint(0, 99)
  	p.currentRoom = room_id
  	p.save()