import tkinter as tk
from tkinter import ttk
from com_connection import ComPort


class PortConfigurationFrame(ttk.Frame):
    def __init__(self, container, app):
        super().__init__(container)
        self.app = app
        self.param_dict = {
            'Send Timeout': tk.IntVar(value=2),
            'Receive Timeout': tk.IntVar(value=5),
            'Port': tk.StringVar(value='COM5'),
            'Baud Rate': tk.IntVar(value=9600),
            'Data Bits': tk.IntVar(value=8),
            'Parity': tk.StringVar(value='Even'),
            'Stop Bits': tk.DoubleVar(value=2.0)
        }
        options = {'padx': 5, 'pady': 5}

        # Frame with default settings buttons:
        self.default_settings_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.default_settings_frame.grid(row=0, column=0, **options)

        # Add buttons to frame
        self.default_config_1 = tk.Button(self.default_settings_frame, text="Default COM",
                                          command=self.insert_default_settings)
        self.default_config_1.grid(row=0, column=0, **options)
        self.default_config_2 = tk.Button(self.default_settings_frame, text="Test Send",
                                          command=self.send_some_info)
        self.default_config_2.grid(row=0, column=1, **options)

        # Frame for inserting timeout params:
        self.timeout_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.timeout_frame.grid(row=1, column=0, **options)

        # Timeout entries
        self.send_timeout_entry = tk.Entry(self.timeout_frame, textvariable=self.param_dict['Send Timeout'])
        self.send_timeout_entry.grid(row=0, column=1, **options)
        self.receive_timeout_entry = tk.Entry(self.timeout_frame, textvariable=self.param_dict['Receive Timeout'])
        self.receive_timeout_entry.grid(row=1, column=1, **options)

        # Timeout labels
        tk.Label(self.timeout_frame, text="Send:").grid(row=0, column=0, sticky=tk.W, **options)
        tk.Label(self.timeout_frame, text="Seconds (1-30)").grid(row=0, column=2, sticky=tk.W, **options)
        tk.Label(self.timeout_frame, text="Receive:").grid(row=1, column=0, sticky=tk.W, **options)
        tk.Label(self.timeout_frame, text="Seconds (1-120)").grid(row=1, column=2, sticky=tk.W, **options)

        # Frame for configuration options
        self.com_options_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.com_options_frame.grid(row=0, column=1, rowspan=2, **options)

        # Labels
        tk.Label(self.com_options_frame, text="Port:").grid(row=0, column=0, sticky=tk.W, **options)
        tk.Label(self.com_options_frame, text="Baud Rate:").grid(row=1, column=0, sticky=tk.W, **options)
        tk.Label(self.com_options_frame, text="Data Bits:").grid(row=2, column=0, sticky=tk.W, **options)
        tk.Label(self.com_options_frame, text="Parity:").grid(row=3, column=0, sticky=tk.W, **options)
        tk.Label(self.com_options_frame, text="Stop Bits:").grid(row=4, column=0, sticky=tk.W, **options)

        # Combobox
        self.port_combobox = ttk.Combobox(self.com_options_frame, textvariable=self.param_dict['Port'])
        self.port_combobox['values'] = ('COM1', 'COM2', 'COM3', 'COM4', 'COM5')
        self.port_combobox.grid(row=0, column=1, **options)
        self.baud_rate_combobox = ttk.Combobox(self.com_options_frame, textvariable=self.param_dict['Baud Rate'])
        self.baud_rate_combobox['values'] = (2400, 4800, 9600, 19200, 115200)
        self.baud_rate_combobox.grid(row=1, column=1, **options)
        self.data_bits_combobox = ttk.Combobox(self.com_options_frame, textvariable=self.param_dict['Data Bits'])
        self.data_bits_combobox['values'] = (5, 7, 8)
        self.data_bits_combobox.grid(row=2, column=1, **options)
        self.parity_combobox = ttk.Combobox(self.com_options_frame, textvariable=self.param_dict['Parity'])
        self.parity_combobox['values'] = ('None', 'Even', 'Odd', 'Mark', 'Space')
        self.parity_combobox.grid(row=3, column=1, **options)
        self.stop_bits_combobox = ttk.Combobox(self.com_options_frame, textvariable=self.param_dict['Stop Bits'])
        self.stop_bits_combobox['values'] = (1, 1.5, 2)
        self.stop_bits_combobox.grid(row=4, column=1, **options)

        # Buttons for connect
        self.connect_buttons_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.connect_buttons_frame.grid(row=3, column=0, columnspan=2)

        # Creating connection button
        self.connect_button = tk.Button(self.connect_buttons_frame, text="Connect",
                                        command=self.on_connect)
        self.connect_button.grid(row=0, column=0, **options)
        self.disconnect_button = tk.Button(self.connect_buttons_frame, text="Disconnect",
                                           command=self.on_disconnect)
        self.disconnect_button.grid(row=0, column=1, **options)

        # packing our frame
        self.pack()

    def insert_default_settings(self):
        self.param_dict['Send Timeout'].set(2)
        self.param_dict['Receive Timeout'].set(5)
        self.param_dict['Port'].set('COM5')
        self.param_dict['Baud Rate'].set(9600)
        self.param_dict['Data Bits'].set(8)
        self.param_dict['Parity'].set('Even')
        self.param_dict['Stop Bits'].set(2)

    def get_configuration(self):
        return self.param_dict

    def on_connect(self):
        if self.app.com_port:
            return 0
        connection_config = {
            'Port': self.param_dict['Port'].get(),
            'Baud Rate': self.param_dict['Baud Rate'].get(),
            'Data Bits': self.param_dict['Data Bits'].get(),
            'Parity': self.param_dict['Parity'].get(),
            'Stop Bits': self.param_dict['Stop Bits'].get(),
            'Send Timeout': self.param_dict['Send Timeout'].get(),
            'Read Timeout': self.param_dict['Receive Timeout'].get()
        }
        com_port = ComPort(**connection_config)
        self.app.set_com_port(com_port)

    def on_disconnect(self):
        self.app.com_port.close()
        self.app.com_port = None

    def send_some_info(self):
        if self.app.com_port:
            self.app.com_port.send_message("Hello")

