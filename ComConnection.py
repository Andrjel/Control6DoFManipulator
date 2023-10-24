import serial
import time
from dataclasses import dataclass


@dataclass
class ComPortParams(serial.Serial):
    byte_size_params = {
        5: serial.FIVEBITS,
        7: serial.SEVENBITS,
        8: serial.EIGHTBITS
    }
    parity_params = {
        'None': serial.PARITY_NONE,
        'Even': serial.PARITY_EVEN,
        'Odd': serial.PARITY_ODD,
        'Mark': serial.PARITY_MARK,
        'Space': serial.PARITY_SPACE
    }
    stop_bits_params = {
        1: serial.STOPBITS_ONE,
        1.5: serial.STOPBITS_ONE_POINT_FIVE,
        2: serial.STOPBITS_TWO
    }


class ComPort(serial.Serial):
    def __init__(self, **kwargs):
        self.__port_name = kwargs['Port']
        self.__baud_rate = kwargs['Baud Rate']
        self.__bytesize = ComPortParams.byte_size_params[kwargs['Data Bits']]
        self.__parity = ComPortParams.parity_params[kwargs['Parity']]
        self.__stopbits = ComPortParams.stop_bits_params[kwargs['Stop Bits']]
        self.__send_timeout = kwargs['Send Timeout']
        self.__read_timeout = kwargs['Read Timeout']
        super().__init__(self.__port_name, baudrate=self.__baud_rate, bytesize=self.__bytesize,
                         parity=self.__parity, stopbits=self.__stopbits,
                         timeout=self.__read_timeout, write_timeout=self.__send_timeout)


def main():
    pass


if __name__ == "__main__":
    main()
