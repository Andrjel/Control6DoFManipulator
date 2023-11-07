import tkinter as tk
from tkinter import ttk
from functools import partial


class XYZFrame(tk.Frame):
    def __init__(self, container, app):
        super().__init__(container)
        self.app = app
        options = {'padx': 5, 'pady': 5}

        self.command_frame = tk.Frame(self, background='grey', highlightthickness=1, **options)
        self.command_frame.grid(row=0, column=0)
        tk.Label(self.command_frame, text='Command').grid(row=0, column=0, **options)
        xyz_entry = []
        xyz_var = {}
        for idx, ori in enumerate(['x', 'y', 'z']):
            xyz_var[ori] = tk.StringVar()
            xyz_entry.append(tk.Entry(self.command_frame, textvariable=xyz_var[ori]))
            xyz_entry[idx].grid(row=1, column=idx, **options)

        self.pack()
