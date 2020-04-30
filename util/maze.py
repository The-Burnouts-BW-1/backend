import random
from PIL import Image
imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))
pixels = image.load()
mx = 10
my = 10  # width and height of the maze
maze = [[0 for x in range(mx)] for y in range(my)]
direction_x = [0, 1, 0, -1]
direction_y = [-1, 0, 1, 0]  # directions to move in the maze


def GenerateMaze(size_x, size_y):  # cell location
    maze[size_y][size_x] = 1
    while True:
        # find a new cell to add
        nlst = []  # list of available neighbors
        for i in range(4):
            next_x = size_x + direction_x[i]  # next x location
            next_y = size_y + direction_y[i]  # next y location
            if next_x >= 0 and next_x < mx and next_y >= 0 and next_y < my:
                if maze[next_y][next_x] == 0:
                    # of occupied neighbors of the candidate cell must be 1
                    center = 0
                    for j in range(4):
                        ex = next_x + direction_x[j]
                        ey = next_y + direction_y[j]
                        if ex >= 0 and ex < mx and ey >= 0 and ey < my:
                            if maze[ey][ex] == 1:
                                center += 1
                    if center == 1:
                        nlst.append(i)
        # if 1 or more available neighbors then randomly select one and add
        if len(nlst) > 0:
            ir = nlst[random.randint(0, len(nlst) - 1)]
            size_x += direction_x[ir]
            size_y += direction_y[ir]
            GenerateMaze(size_x, size_y)
        else:
            break


GenerateMaze(0, 0)
# paint the maze
for ky in range(imgy):
    for kx in range(imgx):
        m = maze[my * ky // imgy][mx * kx // imgx] * 255
        pixels[kx, ky] = (m, m, m)
image.save("RandomMaze_" + str(mx) + "x" + str(my) + ".png", "PNG")
