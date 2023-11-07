import tkinter as tk
from tkinter import ttk
from functools import partial
from time import sleep


class JogOperationFrame(tk.Frame):
    def __init__(self, container, app):
        super().__init__(container)
        self.app = app
        options = {'padx': 5, 'pady': 5}
        self.joints_move = {
            "Waist": "DJ 1, ",
            "Shoulder": "DJ 2, ",
            "Elbow": "DJ 3, ",
            "Twist": "DJ 4, ",
            "Pitch": "DJ 5, ",
            "Roll": "DJ 6, "
        }
        # frame with jog parts
        self.default_settings_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1,)
        self.default_settings_frame.grid(row=0, column=0, **options)

        # Labels
        tk.Label(self.default_settings_frame, text="Waist").grid(row=0, column=0, **options)
        tk.Label(self.default_settings_frame, text="Shoulder").grid(row=1, column=0,  **options)
        tk.Label(self.default_settings_frame, text="Elbow").grid(row=2, column=0, **options)
        tk.Label(self.default_settings_frame, text="Twist").grid(row=3, column=0,  **options)
        tk.Label(self.default_settings_frame, text="Pitch").grid(row=4, column=0,  **options)
        tk.Label(self.default_settings_frame, text="Roll").grid(row=5, column=0,  **options)
        # Arrow buttons
        self.left_waist = tk.Button(self.default_settings_frame, text="🠸", command=self.move_waist_left)
        self.left_waist.grid(row=0, column=1, **options)
        self.right_waist = tk.Button(self.default_settings_frame, text="🠺", command=self.move_waist_right)
        self.right_waist.grid(row=0, column=2, **options)

        self.left_shoulder = tk.Button(self.default_settings_frame, text="🠸", command=self.move_shoulder_left)
        self.left_shoulder.grid(row=1, column=1, **options)
        self.right_shoulder = tk.Button(self.default_settings_frame, text="🠺", command=self.move_shoulder_right)
        self.right_shoulder.grid(row=1, column=2, **options)

        self.left_elbow = tk.Button(self.default_settings_frame, text="🠸", command=self.move_elbow_left)
        self.left_elbow.grid(row=2, column=1, **options)
        self.right_elbow = tk.Button(self.default_settings_frame, text="🠺", command=self.move_elbow_right)
        self.right_elbow.grid(row=2, column=2, **options)

        self.left_twist = tk.Button(self.default_settings_frame, text="🠸", command=self.move_twist_left)
        self.left_twist.grid(row=3, column=1, **options)
        self.right_twist = tk.Button(self.default_settings_frame, text="🠺", command=self.move_twist_right)
        self.right_twist.grid(row=3, column=2, **options)

        self.left_pitch = tk.Button(self.default_settings_frame, text="🠸", command=self.move_pitch_left)
        self.left_pitch.grid(row=4, column=1, **options)
        self.right_pitch = tk.Button(self.default_settings_frame, text="🠺", command=self.move_pitch_right)
        self.right_pitch.grid(row=4, column=2, **options)

        self.left_roll = tk.Button(self.default_settings_frame, text="🠸", command=self.move_roll_left)
        self.left_roll.grid(row=5, column=1, **options)
        self.right_roll = tk.Button(self.default_settings_frame, text="🠺", command=self.move_roll_right)
        self.right_roll.grid(row=5, column=2, **options)

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

        self.config_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1,
                                     width=100, height=100)
        self.config_frame.grid(row=0, column=1, **options)
        tk.Label(self.config_frame, text="Gripper", width=10).grid(row=0, column=0, **options)
        self.grip_open = tk.Button(self.config_frame, text="Open", command=self.open_gripper)
        self.grip_open.grid(row=1, column=0, **options)
        self.grip_close = tk.Button(self.config_frame, text="Close", command=self.close_gripper)
        self.grip_close.grid(row=2, column=0, **options)

        self.pack()

    def set_speed(self, speed):
        if self.app.com_port:
            self.app.com_port.send_message(f"SP {speed}")
            sleep(0.2)

    def close_gripper(self):
        if self.app.com_port:
            self.app.com_port.send_message("GC")

    def open_gripper(self):
        if self.app.com_port:
            self.app.com_port.send_message("GO")

    def move_joint(self, joint, direction):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move[joint] + direction)

    def move_waist_left(self):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move["Waist"] + "-" + str(self.jog_increment.get()))

    def move_waist_right(self):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move["Waist"] + str(self.jog_increment.get()))

    def move_shoulder_left(self):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move["Shoulder"] + "-" + str(self.jog_increment.get()))

    def move_shoulder_right(self):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move["Shoulder"] + str(self.jog_increment.get()))

    def move_elbow_left(self):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move["Elbow"] + "-" + str(self.jog_increment.get()))

    def move_elbow_right(self):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move["Elbow"] + str(self.jog_increment.get()))

    def move_twist_left(self):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move["Twist"] + "-" + str(self.jog_increment.get()))

    def move_twist_right(self):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move["Twist"] + str(self.jog_increment.get()))

    def move_pitch_left(self):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move["Pitch"] + "-" + str(self.jog_increment.get()))

    def move_pitch_right(self):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move["Pitch"] + str(self.jog_increment.get()))

    def move_roll_left(self):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move["Roll"] + "-" + str(self.jog_increment.get()))

    def move_roll_right(self):
        if self.app.com_port:
            self.app.com_port.send_message(self.joints_move["Roll"] + str(self.jog_increment.get()))