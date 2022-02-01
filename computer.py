"""! 
	@file     computer.py
    @brief    Script to run the user interaction and communication interface
    @author   Nick De Simone, Jacob-Bograd, Horacio Albarran
    @date     January 30, 2022
"""

import serial
import numpy as np
import keyboard


class UInterface:
	'''!
    @brief   This class will provide with the result for the User Interface input
    @details This class allows the user to interact with the code by providing
				certain commands that will yield with some of the properties of 
				the Encoder as defined in the introduction of this file
    '''
	# constant defining state 0
    S0_INIT            =  0
    
    # constant defining state 1
    S1_Update_Input    =  1
    
    ## Constant defining State 2
    S2_Update_Input    =  2
    
    def __init__(self):
        '''
        @brief It creates an object function which allows a user to interact with the code
        '''
		
		# Setting a variable for keyboard response
		self.keyboard = keyboard
		
        # It creates a variable with the Shares variables encapsule in it
        self.Shares = Shares
        
        # init with a given baudrate
        self.uart = pyb.UART(2)
    
        # The state to run in the beginnig of the iteration
        self.state = self.S0_INIT
		
	def transitionTo(self, newState):
        '''
        @brief      Updates the variable defining the next state to run
        '''
        self.state = newState
    
    def Allowable_Input(self):
        '''
        @brief It creates an object with the allowable User inputs
        '''
        print (' The possible inputs are, notice they all are lower case letters: ')
        print ( 'z = Zero the Encoder Position')
        print ( 'p = Print out the Encoder position ')
        print ( 'd = Print out delta of the Encoder')
        
    def run(self):
        '''
        @brief   It runs the the User_Interface class
        @details It will continuosly check for an input provided by the user
        '''
        
        self.Input = self.uart.any()     #It will check for any input provided by the user
       
        if self.Input:
            if (self.state == self.S0_INIT):
                self.transitionTo(self.S1_Update_Input)     
				
            elif (self.state == self.S1_Update_Input):
				# Reading the ASCII value on the REPL
                self.Value = self.uart.readchar()
				
                if self.Value == 100:                                   # Checks if the input provided is "d"
                    print (' The Encoder delta value is {:0.2f}'.format(self.Shares.Delta))
                    self.transitionTo(self.S2_Update_Input)
                elif self.Value == 122:                                 # Checks if the input provided is "z"
                    self.Shares.En_Update = 0
                    print ( ' The Encoder position has been set to {:0.2f}'.format(self.Shares.En_Update))
                    self.transitionTo(self.S2_Update_Input)
                elif self.Value == 112:                                 # Checks if the input provided is "p"
                    print ( ' The Encoder position is {:0.2f}'.format(self.Shares.En_Update))
                    self.transitionTo(self.S2_Update_Input)
                else:
                    print ( 'Please refer to the allowable inputs')
                    self.Allowable_Input()
                    self.transitionTo(self.S2_Update_Input)
					
					
            elif (self.state == self.S2_Update_Input):
                self.Value = self.uart.readchar()
                if self.Value == 100:
                    print (' The Encoder delta value is {:0.2f}'.format(self.Shares.Delta))
                    self.transitionTo(self.S1_Update_Input)
                elif self.Value == 122:
                    self.Shares.En_Update = 0 
                    print ( ' The Encoder position has been set to {:0.2f}'.format(self.Shares.En_Update))
                    self.transitionTo(self.S1_Update_Input)
                elif self.Value == 112:
                    print ( ' The Encoder position is {:0.2f}'.format(self.Shares.En_Update))
                    self.transitionTo(self.S1_Update_Input)
                else:
                    print ( 'Please refer to the allowable inputs')
                    self.Allowable_Input()
                    self.transitionTo(self.S1_Update_Input)    
					
					
            else:
                print ('Undefined input')  
				
        else:
			print('No input found on the REPL')
            pass
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

	# def main(self):
		# '''
        # @brief 
        # '''
		# self.data = []
		
		# # it initialized the serial port as well as defining it
		# with serial.Serial('COM5', 115200) as self.s_port:
			# self.s_port.write(b"main()") # send the main command
			# print("WAITING")
			# self.s_port.write(b"1024")  # send the test value over
			# while True:
				# self.temp = self.s_port.readline()
				# print(self.temp)
				# if self.temp == b"DONE":
					# break #we are done

		# print("just finished the with")
				# #if temp != "DONE":
				# #    data.append(temp)
				# #else:
				# #    break


# if __name__ == '__main__':
    # Trial_Run = UInterface()
	# Trial_Run.main()
		#
		
		
		
	
	
	
	
	
