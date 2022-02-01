"""! 
	@file     computer.py
    @brief    Script to run the user interaction and communication interface
    @author   Nick De Simone, Jacob-Bograd, Horacio Albarran
    @date     January 30, 2022
"""

import serial
import numpy as np



def main(self):
	'''
	@brief 
	'''
	self.data = []
	
	# it initialized the serial port as well as defining it
	with serial.Serial('COM5', 115200) as self.s_port:
		self.s_port.write(b"main()") # send the main command
		print("WAITING")
		self.s_port.write(b"1024")  # send the test value over
		while True:
			self.temp = self.s_port.readline()
			print(self.temp)
			if self.temp == b"DONE":
				break #we are done

	print("just finished the with")
			#if temp != "DONE":
			#    data.append(temp)
			#else:
			#    break


if __name__ == '__main__':
    Trial_Run = UInterface()
	Trial_Run.main()
		
		
		
		
	
	
	
	
	
