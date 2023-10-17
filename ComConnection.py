import serial
import time


class ComPort:
    def __init__(self, port_name: str):
        self.__ser = serial.Serial(port_name, baudrate=9600, bytesize=serial.EIGHTBITS,
                                   parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE
                                   )

    def open_port(self):
        self.__ser.open()

    def close_port(self):
        self.__ser.close()

    def send_message(self, message: str):
        self.__ser.write(message)


def main():
    pass


if __name__ == "__main__":
    main()
