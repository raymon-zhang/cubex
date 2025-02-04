from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit1 = MotorKit()
kit2 = MotorKit(address=0x61)
kit3 = MotorKit(address=0x62)

while True:
    kit1.stepper1.onestep(direction=stepper.FORWARD)
    kit1.stepper2.onestep(direction=stepper.FORWARD)
    kit2.stepper1.onestep(direction=stepper.FORWARD)
    kit2.stepper2.onestep(direction=stepper.FORWARD)
    kit3.stepper1.onestep(direction=stepper.FORWARD)
    kit3.stepper2.onestep(direction=stepper.FORWARD)
