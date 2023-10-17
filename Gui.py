import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Roboty Przemyslowe')
        self.geometry('400x500')


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
