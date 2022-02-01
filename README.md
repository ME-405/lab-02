# Cal Poly ME-405
## Lab 02
Jacob Bograd, Nick De Simone, Horacio Albarran

Documentation https://me-405.github.io/lab-02/

---
#### This lab runs step response tests on a closed loop motor control system
    The controller receives values for the proportional gain constant, Kp, over UART.
    The controller then calculates a suitable PWM signal to have the motor approach 
    the desired positional setpoint. 
    It determines positional error using a quadrature encoder and adjusts the PWM 
    signal accordingly.
    Once the setpoint is reached, the cumulative time and position data are sent back 
    to the computer, where they are plotted against one another.
    See the figures below for observation of Position vs. Time for four different values of Kp.

---

![Kp = 0.5](Images/K_p%200.5.png)![Kp = 0.6](Images/K_p%200.6.png)
![Kp = 0.7](Images/K_p%200.7.png)![kp = 3  ](Images/K_p%203%20we%20had%20to%20hold%20it.png)
    
**NOTE**
Kp = 3 is too large, as it causes the flywheel to oscillate, seemingly indefinitely, about the setpoint.
We found it necessary to physically grab the flywheel to stop on the setpoint when Kp = 3.
This represents an undesirable proportional gain and suggests the gain should be held between 0.1-0.7.


