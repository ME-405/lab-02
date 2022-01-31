# import the required classes
from Motor import MotorDriver
from encoder import Encoder
from pyb import Pin
from pyb import UART
import pyb
import time
import utime


class closedLoopController:

    def __init__(self, input_interval, encoder, motor
                 # encoder_pin1, encoder_pin2, encoder_timer,
                 # motor_enable, motor_pin1, motor_pin2, motor_timer
                 ):
        '''

        '''

        # set the setpoint and gain both to 0
        self.final_point = 0
        self.kp = 0
        self.current_time = 0
        # self.encoder_pin1 = encoder_pin1
        # self.encoder_pin2 = encoder_pin2
        # self.encoder_timer = encoder_timer
        # self.encoder = Encoder(encoder_pin1, encoder_pin2, encoder_timer, 1, 2)
        self.encoder = encoder
        # Instantiated the objects for the chosen Motor,
        # self.motor_enable = motor_enable
        # self.motor_pin1 = motor_pin1
        # self.motor_pin2 = motor_pin2
        # self.motor_timer = motor_timer

        # self.motor = MotorDriver(self.motor_enable, self.motor_pin1, self.motor_pin2, self.motor_timer, 1, 2)

        self.motor = motor
        self.gain = 0  # the gain will be updated in a function
        self.start_time = utime.ticks_ms()  # the staring time
        self.interval = input_interval  # the interval of the milliseconds
        self.nextTime = utime.ticks_add(self.start_time, self.interval)
        self.uart = UART(2)
        self.uart.init(115200)
        self.time_list = []
        self.encoder_list = []

    def control_algorithm(self):
        # self.update_setpoint()  # prompt the user for an updated setpoint
        # self.update_kp()  # prompt the user for a new kp
        # print("setting values")
        #self.kp = .1
        #self.kp = float(input())
        input_kp(self)
        self.final_point = 16384
        self.encoder.set_position(0)  # zero out the encoder value
        # print("values set")
        while True:
            # self.kp = float(input())
            self.encoder.update()  # update the encoder value
            error = self.final_point - self.encoder.current_pos  # get the error
            # print("error = ", error)
            if error == 0:
                # print("DEBUG: ERROR IS NOW 0")
                self.motor.disable()  # disable the motor
                break
            else:
                self.current_time = utime.ticks_ms()
                if utime.ticks_diff(self.current_time, self.nextTime) >= 0:
                    actuation = (error * self.kp)  # get the actuation
                    if actuation >= 80:
                        self.motor.set_duty_cycle(80)
                    elif 30 >= actuation > 5:
                        self.motor.set_duty_cycle(30)
                    elif -30 <= actuation < 5:
                        self.motor.set_duty_cycle(-30)
                    elif actuation <= -80:
                        self.motor.set_duty_cycle(-80)
                    elif -5 <= actuation <= 5:
                        #        print("DEBUG: I HAVE FINISHED")
                        self.motor.disable()
                        break
                    else:
                        self.motor.set_duty_cycle(actuation)
                self.update_list()  # update the list position\
                utime.sleep_ms(self.interval)
                #self.nextTime = utime.ticks_add(self.nextTime, self.interval)  # update the next time

        self.print_list()  # print out the list when we are done

    def update_setpoint(self):
        self.final_point = int(input("Please enter the setpoint"))

    def update_interval(self):
        self.interval = int(input("Please enter the interval"))

    def update_list(self):
        self.encoder.update()
        encoder_value = self.encoder.current_pos
        timestamp = utime.ticks_diff(utime.ticks_ms(), self.start_time)
        self.time_list.append(timestamp)
        self.encoder_list.append(encoder_value)

    # print("DEBUG: ", timestamp, encoder_value)

    def update_kp(self):
        self.kp = float(input("Please enter kp"))

    def print_list(self):
        data = zip(self.time_list, self.encoder_list)
        for numbers in data:
            print(*numbers)
        print("DONE")
        # clear the differnt lists
        self.time_list.clear()
        self.encoder_list.clear()
        # print(self.time_list, self.encoder_list)
        #  for index in self.time_list:
        #  print("time, ", index)
        #  for index in self.encoder_list:
        #  print("encoder, ", index)
    # for index in self.time_list:
    #    print(self.time_list[index], " , ", self.encoder_list[index])


def input_kp(self):
    while self.uart.any == 0:
        utime.sleep_us(50)
    self.kp = self.uart.read()
    self.kp = self.kp.decode()

#   check = self.uart.any()
#   while check != 0:
#       check = self.uart.any()
#     utime.sleep_us(20)

#  raw_value = self.uart.readline()
#  modified_value = raw_value  # offset for ascii values
#   self.kp = modified_value

#
