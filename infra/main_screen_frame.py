import tkinter as tk
from tkinter import ttk


class WczytywanieDanych(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.app = container
        options = {'padx': 5, 'pady': 5}
        # Add frame for sending data to robot
        self.send_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.send_frame.grid(row=1, column=0, **options)
        tk.Label(self.send_frame, text="Send:").grid(row=0, column=0, **options)
        self.entry_var = tk.StringVar()
        self.send_entry = tk.Entry(self.send_frame, textvariable=self.entry_var)
        self.send_entry.grid(row=0, column=1, **options)
        # # buttons for send
        self.send_button = tk.Button(self.send_frame, text="Send", command=self.send_writen_command)
        self.send_button.grid(row=0, column=2, **options)
        # # Add frame for reading data from robot
        self.read_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.read_frame.grid(row=2, column=0, **options)
        self.table = ttk.Treeview(self.read_frame, columns=('Timestamp', 'Data'), show='headings',
                                  height=5)
        self.table.heading('Timestamp', text='Timestamp')
        self.table.heading('Data', text='Data')
        self.table.pack()
        self.grid(row=1, column=0)

    def send_writen_command(self):
        if self.entry_var and self.app.com_port is not None:
            comm = self.entry_var.get() + '\r'
            self.app.com_port.write(comm.encode())

