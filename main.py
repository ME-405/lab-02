''' @file                       main.py
    @brief                      File that runs the encoder and motor
    @author                     Nick De Simone, Jacob-Bograd, Horacio Albarran
    @date                       January 22, 2022
'''

# Importing libraries and classes,
from Motor import MotorDriver
from encoder import Encoder
from closedLoopControl import closedLoopController as closed_loop
from pyb import Pin
import pyb
import time

# Instantiated object for the encoder as well as timer,
encoderPin1 = pyb.Pin(pyb.Pin.cpu.C6)
encoderPin2 = pyb.Pin(pyb.Pin.cpu.C7)
EncTimer = 8
EncoderDriver = Encoder(encoderPin1, encoderPin2, EncTimer, 1, 2)

# Instantiated the objects for the chosen Motor,
motorEnable = pyb.Pin(pyb.Pin.cpu.A10, pyb.Pin.IN, pyb.Pin.PULL_UP)
motorPin1 = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
motorPin2 = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
motorTimer = pyb.Timer(3, freq=20000)
Motor = MotorDriver(motorEnable, motorPin1, motorPin2, motorTimer, 1, 2)


def main():
    input_interval = int(input("Enter the interval"))
    clc = closed_loop(input_interval, EncoderDriver, Motor)

    Motor.enable()

    try:
        clc.control_algorithm()
    except KeyboardInterrupt:
        Motor.disable()
    print('out of loop')


if __name__ == '__main__':
    main()
