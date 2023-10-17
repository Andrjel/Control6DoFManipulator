import Gui
from ComConnection import ComPort
from Gui import *
# TODO: parametryzacja portu - okno
# TODO: obsluga wysylania i odbioru danych przez port szeregowy
# TODO: Wysylanie komend z "reki"
# TODO: Jog operator do sterowania ruchem robota w przestrzeni zmiennych konfiguracyjnych


def main():
    # Starting gui
    # Create gui object and start our app
    app = App()
    app.mainloop()
    # com = ComPort("COM5")
    # com.send_message(b"Hello")


if __name__ == "__main__":
    main()
