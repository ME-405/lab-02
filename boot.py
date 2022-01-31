"""! 
	@file     boot.py
    @brief    
    @author   Nick De Simone, Jacob-Bograd, Horacio Albarran
    @date     January 30, 2022
"""

## ------------------------------------------------------->   IS THIS THE SAME AS THE MAIN FILE???   <--------------------------------------------------------------------

# Importing libraries and classes
from Motor import MotorDriver
from encoder import Encoder
from closedLoopControl import closedLoopController as closed_loop
from pyb import Pin
import pyb
import time

# Instantiated object for the encoder as well as timer,
encoderPin1 = pyb.Pin(pyb.Pin.board.PC6)
encoderPin2 = pyb.Pin(pyb.Pin.board.PC7)
EncTimer = 8
EncoderDriver = Encoder(encoderPin1, encoderPin2, EncTimer, 1, 2)

# Instantiated the objects for the chosen Motor,
motorEnable = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.IN, pyb.Pin.PULL_UP)
motorPin1 = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
motorPin2 = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
motorTimer = pyb.Timer(3, freq=20000)
Motor = MotorDriver(motorEnable, motorPin1, motorPin2, motorTimer, 1, 2)


input_interval = 10
#input_interval = int(input("Enter the interval"))
clc = closed_loop(input_interval, EncoderDriver, Motor)
#print("about to enable the motor")
Motor.enable()
clc.control_algorithm()
#print("just about to go into while")
