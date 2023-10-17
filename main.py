from ComConnection import ComPort


def main():
    com = ComPort("COM5")
    com.send_message(b"Hello")


if __name__ == "__main__":
    main()
