from nicegui import ui
import time

import kociemba
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import util
import interface

kit1 = MotorKit()
kit2 = MotorKit(address=0x61)
kit3 = MotorKit(address=0x62)

STEPS = 50
STEP_DELAY = 0


solution_string = "asdf"


def solve_cube():
    for step in solution_string.split(" "):
        double = False
        reverse = False
        if len(step) == 2:
            if step[1] == "'":
                reverse = True
            elif step[1] == "2":
                double = True

        motor_dict = {
            "U": kit1.stepper1,
            "R": kit1.stepper2,
            "L": kit2.stepper1,
            "B": kit2.stepper2,
            "F": kit3.stepper1,
            "D": kit3.stepper2,
        }
        motor = motor_dict[step[0]]

        if double:
            for i in range(STEPS * 2):
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
    global solution_string
    util.take_images()
    cube_state = util.process()
    solution_string = kociemba.solve(cube_state)


# def solve():
#     print(solution_string)


ui.html(interface.html)

ui.add_css(interface.css)

with ui.teleport(".scan"):
    ui.button("SCAN", on_click=scan)

with ui.teleport(".solve"):
    ui.button("SOLVE", on_click=solve_cube)

ui.run()
