import tkinter as tk
from tkinter import ttk
from functools import partial
from time import sleep


class XYZFrame(tk.Frame):
    def __init__(self, container, app):
        super().__init__(container)
        self.app = app
        options = {'padx': 5, 'pady': 5}

        self.image_frame = tk.Frame(self, highlightbackground='grey', highlightthickness=1, **options)
        self.image_frame.grid(row=0, column=0, **options)
        self.image = tk.PhotoImage(file='osie.png')
        self.image_label = tk.Label(self.image_frame, image=self.image).pack()
        self.button_x_plus = tk.Button(self.image_frame, text="X+", command=self.x_plus)
        self.button_x_plus.place(x=100, y=120)
        self.button_x_minus = tk.Button(self.image_frame, text="X-", command=self.x_minus)
        self.button_x_minus.place(x=75, y=120)
        self.button_y_plus = tk.Button(self.image_frame, text="Y+", command=self.y_plus)
        self.button_y_plus.place(x=110, y=10)
        self.button_y_minus = tk.Button(self.image_frame, text="Y-", command=self.y_minus)
        self.button_y_minus.place(x=85, y=10)
        self.button_z_plus = tk.Button(self.image_frame, text="Z+", command=self.z_plus)
        self.button_z_plus.place(x=0, y=60)
        self.button_z_minus = tk.Button(self.image_frame, text="Z-", command=self.z_minus)
        self.button_z_minus.place(x=0, y=85)

        self.command_frame = tk.Frame(self, highlightbackground='grey', highlightthickness=1, **options)
        self.command_frame.grid(row=0, column=1)
        tk.Label(self.command_frame, text='Command').grid(row=0, column=0, columnspan=3, **options)
        self.xyz_entry = []
        self.xyz_var = {}
        for idx, ori in enumerate(['X', 'Y', 'Z']):
            self.xyz_var[ori] = tk.StringVar()
            self.xyz_entry.append(tk.Entry(self.command_frame, textvariable=self.xyz_var[ori], width=3))
            tk.Label(self.command_frame, text=ori).grid(row=1, column=idx, **options)
            self.xyz_entry[idx].grid(row=2, column=idx, **options)
        self.send_button = tk.Button(self.command_frame, text="Move", command=self.send_move_command)
        self.send_button.grid(row=3, column=1, **options)

        self.jog_speed_slider_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.jog_speed_slider_frame.grid(row=1, column=0, **options)
        tk.Label(self.jog_speed_slider_frame, text="Jog Speed").grid(row=0, column=1, **options)
        self.jog_speed = tk.IntVar(value=1)
        self.set_speed(self.jog_speed.get())
        self.speed_slider = tk.Scale(self.jog_speed_slider_frame, from_=1, to=10, orient=tk.HORIZONTAL,
                                     tickinterval=1, length=225, variable=self.jog_speed, command=self.set_speed)
        self.speed_slider.grid(row=1, column=0, columnspan=3, **options)

        self.jog_increment_slider_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.jog_increment_slider_frame.grid(row=2, column=0, **options)
        tk.Label(self.jog_increment_slider_frame, text="Jog Increment").grid(row=0, column=1, **options)
        self.jog_increment = tk.IntVar(value=10)
        self.increment_slider = tk.Scale(self.jog_increment_slider_frame, from_=0, to=60, orient=tk.HORIZONTAL,
                                         tickinterval=10, length=225, variable=self.jog_increment,
                                         resolution=5)
        self.increment_slider.grid(row=1, column=0, columnspan=3, **options)

        self.position_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.position_frame.grid(row=1, column=1, **options)
        self.position_box = ttk.Combobox(self.position_frame, values =[i for i in range(1, 10)])
        self.position_box.grid(row=0, column=0, **options)

        self.pack()

    def set_speed(self, speed):
        if self.app.com_port:
            self.app.com_port.send_message(f"SP {speed}")
            sleep(0.2)

    def send_move_command(self):
        if self.app.com_port:
            self.app.com_port.send_message(f"DS {self.xyz_var['X'].get()}, {self.xyz_var['Y'].get()}, "
                                           f"{self.xyz_var['Z'].get()}")

    def x_plus(self):
        if self.app.com_port:
            self.app.com_port.send_message(f"DS {self.jog_increment.get()}, 0, 0")

    def x_minus(self):
        if self.app.com_port:
            self.app.com_port.send_message(f"DS -{self.jog_increment.get()}, 0, 0")

    def y_plus(self):
        if self.app.com_port:
            self.app.com_port.send_message(f"DS 0, {self.jog_increment.get()}, 0")

    def y_minus(self):
        if self.app.com_port:
            self.app.com_port.send_message(f"DS 0, -{self.jog_increment.get()}, 0")

    def z_plus(self):
        if self.app.com_port:
            self.app.com_port.send_message(f"DS 0, 0, {self.jog_increment.get()}")

    def z_minus(self):
        if self.app.com_port:
            self.app.com_port.send_message(f"DS 0, 0, -{self.jog_increment.get()}")
