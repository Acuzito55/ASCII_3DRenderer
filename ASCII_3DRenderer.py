import os
import time
import math
import keyboard

os.system('cls')
vector = []
res = int(input("Select a resolution: "))
if res % 2 == 0:
    res += 1
hres = (res-1)//2
characters = '@$%8&#0QOCaoc<>*;:+~-,"^`'


def sphere(x, y, z, r):
    return x**2 + y**2 + z**2 <= r**2


def cube(x, y, z, r):
    return max([abs(x), abs(y), abs(z)]) <= r


def donut(x, y, z, r, w):
    s = math.sqrt(x**2+y**2)
    return z**2 + (r-s)**2 < w**2


def makeObject(shape, r, w):
    o = (res-1)/2
    for x in range(res):
        vector.append([])
        for y in range(res):
            vector[x].append([])
            for z in range(res):
                if shape == 0:
                    vector[x][y].append(
                        sphere(x-o, y-o, z-o, r))
                if shape == 1:
                    vector[x][y].append(
                        cube(x-o, y-o, z-o, r))
                if shape == 2:
                    vector[x][y].append(
                        donut(x-o, y-o, z-o, r, w))


def renderObject(r, angle1, angle2):
    o = (res-1)/2
    for x in range(res):
        for y in range(res):
            finished = True
            for z in range(res):
                x1 = o + (x-o)*math.cos(angle2) + (z-o)*math.sin(angle2)
                y1 = y
                z1 = o + (z-o)*math.cos(angle2) - (x-o)*math.sin(angle2)

                x2 = x1
                y2 = o + (y1-o)*math.cos(angle1) - (z1-o)*math.sin(angle1)
                z2 = o + (y1-o)*math.sin(angle1) + (z1-o)*math.cos(angle1)

                X = min(max(round(x2), 0), res-1)
                Y = min(max(round(y2), 0), res-1)
                Z = min(max(round(z2), 0), res-1)
                if vector[X][Y][Z]:
                    print(characters[round(z/res*len(characters))], end="")
                    finished = False
                    break
            if finished:
                print(" ", end="")
        print("")


angle1 = 0.0
angle2 = 0.0
stringShape = "Select a shape to render (0: Sphere, 1: Cube, 2: Donut): "
stringRadius = f"Select a radius size (max {hres}, lesser values are recommended): "
stringTorusWidth = "Select a width for the torus (max "
shape = int(input(stringShape))
r = int(input(stringRadius))
w = 0
if shape == 2:
    w = int(input(stringTorusWidth + str(min(hres-r, r)) + "): "))
while shape >= 0 and shape < 3 and r-w >= 0 and r+w <= hres:
    os.system('cls')
    if shape == 0:
        print(f"Sphere of radius {r}:")
    if shape == 1:
        print(f"Cube of radius {r}:")
    if shape == 2:
        print(f"Donut of radius {r} and width {w}:")
    vector = []
    makeObject(shape, r, w)
    print("Use arrow keys to rotate view")
    print("Press space to exit view mode")
    renderObject(r, angle1, angle2)
    while not keyboard.is_pressed('space'):
        if keyboard.is_pressed('left'):
            os.system('cls')
            print("Use arrow keys to rotate view")
            print("Press space to exit view mode")
            angle1 += 0.1
            renderObject(r, angle1, angle2)
        elif keyboard.is_pressed('right'):
            os.system('cls')
            print("Use arrow keys to rotate view")
            print("Press space to exit view mode")
            angle1 -= 0.1
            renderObject(r, angle1, angle2)
        elif keyboard.is_pressed('up'):
            os.system('cls')
            print("Use arrow keys to rotate view")
            print("Press space to exit view mode")
            angle2 += 0.1
            renderObject(r, angle1, angle2)
        elif keyboard.is_pressed('down'):
            os.system('cls')
            print("Use arrow keys to rotate view")
            print("Press space to exit view mode")
            angle2 -= 0.1
            renderObject(r, angle1, angle2)
    os.system("cls")
    shape = int(input(stringShape))
    r = int(input(stringRadius))
    w = 0
    if shape == 2:
        w = int(input(stringTorusWidth + str(min(hres-r, r)) + "): "))
