import tkinter as tk
from tkinter import ttk
from infra.toolbox import ToolBox
from infra.main_screen_frame import WczytywanieDanych


class App(tk.Tk):
    """
        Main app class
    """
    def __init__(self):
        super().__init__()
        self.title('Roboty Przemyslowe')
        self.geometry('500x300')
        self.com_port = None
        ToolBox(self, self)
        WczytywanieDanych(self)
        self.mainloop()

    def set_com_port(self, com_port):
        self.com_port = com_port


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
