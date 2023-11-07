import tkinter as tk
from tkinter import ttk
from functools import partial
from time import sleep


class XYZFrame(tk.Frame):
    def __init__(self, container, app):
        super().__init__(container)
        self.app = app
        options = {'padx': 5, 'pady': 5}

        self.command_frame = tk.Frame(self, highlightbackground='grey', highlightthickness=1, **options)
        self.command_frame.grid(row=0, column=0)
        tk.Label(self.command_frame, text='Command').grid(row=0, column=0, columnspan=3, **options)
        xyz_entry = []
        xyz_var = {}
        for idx, ori in enumerate(['X', 'Y', 'Z']):
            xyz_var[ori] = tk.StringVar()
            xyz_entry.append(tk.Entry(self.command_frame, textvariable=xyz_var[ori], width=3))
            tk.Label(self.command_frame, text=ori).grid(row=1, column=idx, **options)
            xyz_entry[idx].grid(row=2, column=idx, **options)

        self.jog_speed_slider_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.jog_speed_slider_frame.grid(row=1, column=0, columnspan=2, **options)
        tk.Label(self.jog_speed_slider_frame, text="Jog Speed").grid(row=0, column=1, **options)
        self.jog_speed = tk.IntVar(value=1)
        self.set_speed(self.jog_speed.get())
        self.speed_slider = tk.Scale(self.jog_speed_slider_frame, from_=1, to=10, orient=tk.HORIZONTAL,
                                     tickinterval=1, length=225, variable=self.jog_speed, command=self.set_speed)
        self.speed_slider.grid(row=1, column=0, columnspan=3, **options)

        self.jog_increment_slider_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.jog_increment_slider_frame.grid(row=2, column=0, columnspan=2, **options)
        tk.Label(self.jog_increment_slider_frame, text="Jog Increment").grid(row=0, column=1, **options)
        self.jog_increment = tk.IntVar(value=10)
        self.increment_slider = tk.Scale(self.jog_increment_slider_frame, from_=0, to=60, orient=tk.HORIZONTAL,
                                         tickinterval=10, length=225, variable=self.jog_increment,
                                         resolution=5)
        self.increment_slider.grid(row=1, column=0, columnspan=3, **options)

        self.pack()

    def set_speed(self, speed):
        if self.app.com_port:
            self.app.com_port.send_message(f"SP {speed}")
            sleep(0.2)




