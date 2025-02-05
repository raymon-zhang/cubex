from adafruit_motorkit import MotorKit
import time
from adafruit_motor import stepper

kit1 = MotorKit()
# kit2 = MotorKit(address=0x61)
# kit3 = MotorKit(address=0x62)

while True:
    for i in range(50):
        kit1.stepper1.onestep(direction=stepper.FORWARD)
        time.sleep(0.001)
    time.sleep(0.5)
    # time.sleep(0.005)
    # kit1.stepper2.onestep(direction=stepper.FORWARD)
    # kit2.stepper1.onestep(direction=stepper.FORWARD)
    # kit2.stepper2.onestep(direction=stepper.FORWARD)
    # kit3.stepper1.onestep(direction=stepper.FORWARD)
    # kit3.stepper2.onestep(direction=stepper.FORWARD)
