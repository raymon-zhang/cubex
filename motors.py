from nicegui import ui
import pygame
import pygame.camera
from PIL import Image
import numpy as np
import time
import kociemba
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit1 = MotorKit()
kit2 = MotorKit(address=0x61)
kit3 = MotorKit(address=0x62)

PATH_IMG1 = "cam1.png"
PATH_IMG2 = "cam2.png"
STEPS = 50
STEP_DELAY = 0.003

def closest_color(color):
    colors = {
        [255, 0, 0]: "R",
        [0, 255, 0]: "F",
        [0, 0, 0]: "U",
        [0, 0, 255]: "B",
        [255, 100, 0]: "L",
        [255, 255, 0]: "D"
    }

    color_keys = np.array(colors.keys())
    color = np.array(color)

    distances = np.sqrt(np.sum((color_keys-color)**2,axis=1))
    index_of_smallest = np.argmin()
    smallest_distance = colors[index_of_smallest]
    return smallest_distance 

def take_images():
    pygame.camera.init()
    pygame.camera.list_cameras() 

    cam1 = pygame.camera.Camera("/dev/video0",(640,480))
    cam1.start()
    img1 = cam1.get_image()

    cam2 = pygame.camera.Camera("/dev/video1", (640, 480))
    cam2.start()
    img2 = cam2.get_image()

    pygame.image.save(img1, PATH_IMG1)
    pygame.image.save(img2, PATH_IMG2)

def process_cam1():
    img = Image.open(PATH_IMG1)
    pixels = img.load()

    U = []
    R = []
    F = []
    
    U.append(closest_color(pixels[x,y]))
    U.append(closest_color(pixels[x,y]))
    U.append(closest_color(pixels[x,y]))
    U.append(closest_color(pixels[x,y]))
    U.append(closest_color(pixels[x,y]))
    U.append(closest_color(pixels[x,y]))
    U.append(closest_color(pixels[x,y]))
    U.append(closest_color(pixels[x,y]))
    U.append(closest_color(pixels[x,y]))

    R.append(closest_color(pixels[x,y]))
    R.append(closest_color(pixels[x,y]))
    R.append(closest_color(pixels[x,y]))
    R.append(closest_color(pixels[x,y]))
    R.append(closest_color(pixels[x,y]))
    R.append(closest_color(pixels[x,y]))
    R.append(closest_color(pixels[x,y]))
    R.append(closest_color(pixels[x,y]))
    R.append(closest_color(pixels[x,y]))

    F.append(closest_color(pixels[x,y]))
    F.append(closest_color(pixels[x,y]))
    F.append(closest_color(pixels[x,y]))
    F.append(closest_color(pixels[x,y]))
    F.append(closest_color(pixels[x,y]))
    F.append(closest_color(pixels[x,y]))
    F.append(closest_color(pixels[x,y]))
    F.append(closest_color(pixels[x,y]))
    F.append(closest_color(pixels[x,y]))

    return U, R, F

def process_cam2():
    img2 = Image.open(PATH_IMG2)
    pixels = img2.load()

    B = []
    L = []
    D = []
    
    B.append(closest_color(pixels[x,y]))
    B.append(closest_color(pixels[x,y]))
    B.append(closest_color(pixels[x,y]))
    B.append(closest_color(pixels[x,y]))
    B.append(closest_color(pixels[x,y]))
    B.append(closest_color(pixels[x,y]))
    B.append(closest_color(pixels[x,y]))
    B.append(closest_color(pixels[x,y]))
    B.append(closest_color(pixels[x,y]))

    L.append(closest_color(pixels[x,y]))
    L.append(closest_color(pixels[x,y]))
    L.append(closest_color(pixels[x,y]))
    L.append(closest_color(pixels[x,y]))
    L.append(closest_color(pixels[x,y]))
    L.append(closest_color(pixels[x,y]))
    L.append(closest_color(pixels[x,y]))
    L.append(closest_color(pixels[x,y]))
    L.append(closest_color(pixels[x,y]))

    D.append(closest_color(pixels[x,y]))
    D.append(closest_color(pixels[x,y]))
    D.append(closest_color(pixels[x,y]))
    D.append(closest_color(pixels[x,y]))
    D.append(closest_color(pixels[x,y]))
    D.append(closest_color(pixels[x,y]))
    D.append(closest_color(pixels[x,y]))
    D.append(closest_color(pixels[x,y]))
    D.append(closest_color(pixels[x,y]))

    return B, L, D

def process():
    U, R, F = process_cam1()
    B, L, D = process_cam1()
    return ''.join(U) + ''.join(R) + ''.join(F) + ''.join(B) + ''.join(L) + ''.join(D)

def solve_cube(solution):
    for step in solution.split(" "):
        double = False
        reverse = False
        if len(step) == 2:
            if step[1] == "\'":
                reverse = True
            elif step[1] == "2":
                double = True

        motor_dict = {"U": kit1.stepper1, "R": kit1.stepper2, "L": kit2.stepper1, "B": kit2.stepper2, "F": kit3.stepper1, "D": kit3.stepper2}
        motor = motor_dict[step[0]]

        if double:
            for i in range(STEPS*2):
                motor.onestep()
                time.sleep(STEP_DELAY)
        elif reverse:
            for i in range(STEPS):
                motor.onestep(direction=stepper.BACKWARD)
                time.sleep(STEP_DELAY)
        else:
            for i in range(STEPS):
                motor.onestep()
                time.sleep(STEP_DELAY)

def scan():
    take_images()
    cube_state = process()
    solution = kociemba.solve(cube_state)
    solve_cube(solution)


ui.query('h1').style('background-color: red')

ui.html('<h1>hi</h1>')
ui.button('Button', on_click=scan)

ui.run()
