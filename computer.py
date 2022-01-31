import serial
import numpy as np


def main():
    data = []
    with serial.Serial('COM5', 115200) as s_port:
        s_port.write(b"main()") # send the main command
        print("WAITING")
        s_port.write(b"1024")  # send the test value over
        while True:
            temp = s_port.readline()
            print(temp)
            if temp == b"DONE":
                break #we are done

    print("just finished the with")
            #if temp != "DONE":
            #    data.append(temp)
            #else:
            #    break


if __name__ == '__main__':
    main()
