import tkinter as tk
from tkinter import ttk


class ToolBox(ttk.Frame):
    """
        Toolbox in app, here will be fields and methods handling some config windows
    """
    def __init__(self, container):
        super().__init__(container)
        # button for openning com port config
        self.port_config_button = tk.Button(self, text="Configure port",
                                            command=self.open_port_config_window)
        self.port_config_button.pack(side="left")

        self.place(x=0, y=0, width=500, height=25)

    def open_port_config_window(self):
        self.port_window = tk.Toplevel()
        self.port_window.title("Port Configuration")
        self.port_window.geometry("600x220")
        self.port_frame = PortConfigurationFrame(self.port_window)


class PortConfigurationFrame(ttk.Frame):
    """
        Window for port configuration, here we have code to configure and enstablish com connection
    """
    param_dict = {
        'Send Timeout': tk.IntVar,
        'Receive Timeout': tk.IntVar,
        'Port': tk.StringVar,
        'Baud Rate': tk.IntVar,
        'Data Bits': tk.IntVar,
        'Parity': tk.StringVar,
        'Stop Bits': tk.IntVar
    }

    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}
        # frame with default settings buttons:
        self.default_settings_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.default_settings_frame.grid(row=0, column=0, **options)
        # add buttons to frame
        self.default_config_1 = tk.Button(self.default_settings_frame, text="default_1")
        self.default_config_1.grid(row=0, column=0, **options)
        self.default_config_2 = tk.Button(self.default_settings_frame, text="default_2")
        self.default_config_2.grid(row=0, column=1, **options)

        # frame for inserting timeout params:
        self.timeout_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.timeout_frame.grid(row=1, column=0, **options)
        # timeout entries
        self.send_timeout_entry = tk.Entry(self.timeout_frame)
        self.send_timeout_entry.grid(row=0, column=1, **options)
        self.receive_timeout_entry = tk.Entry(self.timeout_frame)
        self.receive_timeout_entry.grid(row=1, column=1, **options)
        # timeout labels
        tk.Label(self.timeout_frame, text="Send:").grid(row=0, column=0, sticky=tk.W, **options)
        tk.Label(self.timeout_frame, text="Seconds (1-30)").grid(row=0, column=2, sticky=tk.W, **options)
        tk.Label(self.timeout_frame, text="Receive:").grid(row=1, column=0, sticky=tk.W, **options)
        tk.Label(self.timeout_frame, text="Seconds (1-120)").grid(row=1, column=2, sticky=tk.W, **options)

        # frame for configuration options
        self.com_options_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.com_options_frame.grid(row=0, column=1, rowspan=2, **options)
        # Labels
        tk.Label(self.com_options_frame, text="Port:").grid(row=0, column=0, sticky=tk.W, **options)
        tk.Label(self.com_options_frame, text="Baud Rate:").grid(row=1, column=0, sticky=tk.W, **options)
        tk.Label(self.com_options_frame, text="Data Bits:").grid(row=2, column=0, sticky=tk.W, **options)
        tk.Label(self.com_options_frame, text="Parity:").grid(row=3, column=0, sticky=tk.W, **options)
        tk.Label(self.com_options_frame, text="Stop Bits:").grid(row=4, column=0, sticky=tk.W, **options)
        # combobox
        self.port_combobox = ttk.Combobox(self.com_options_frame)
        self.port_combobox['values'] = ('COM1', 'COM2', 'COM3', 'COM4', 'COM5')
        self.port_combobox.grid(row=0, column=1, **options)
        self.baud_rate_combobox = ttk.Combobox(self.com_options_frame)
        self.baud_rate_combobox['values'] = (2400, 4800, 9600, 19200, 115200)
        self.baud_rate_combobox.grid(row=1, column=1, **options)
        self.data_bits_combobox = ttk.Combobox(self.com_options_frame)
        self.data_bits_combobox['values'] = (5, 6, 7, 8)
        self.data_bits_combobox.grid(row=2, column=1, **options)
        self.parity_combobox = ttk.Combobox(self.com_options_frame)
        self.parity_combobox['values'] = ('None', 'Even', 'Odd', 'Mark', 'Space')
        self.parity_combobox.grid(row=3, column=1, **options)
        self.stop_bits_combobox = ttk.Combobox(self.com_options_frame)
        self.stop_bits_combobox['values'] = (1, 1.5, 2)
        self.stop_bits_combobox.grid(row=4, column=1, **options)

        # buttons for connect
        self.connect_buttons_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.connect_buttons_frame.grid(row=3, column=0, columnspan=2)
        # creating connection button
        self.connect_button = tk.Button(self.connect_buttons_frame, text="Connect")
        self.connect_button.grid(row=0, column=0, **options)
        self.disconnect_button = tk.Button(self.connect_buttons_frame, text="Disconnect")
        self.disconnect_button.grid(row=0, column=1, **options)

        # packing our frame
        self.pack()


class App(tk.Tk):
    """
        Main app class
    """
    def __init__(self):
        super().__init__()
        self.title('Roboty Przemyslowe')
        self.geometry('800x500')
        # ToolBox
        ToolBox(self)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
