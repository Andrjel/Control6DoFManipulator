import tkinter as tk
from tkinter import ttk
from ComConnection import ComPort


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
        # button for openning jog operation window
        self.jog_operation_button = tk.Button(self, text="Jog Operation",
                                            command=self.open_jog_operation_window)
        self.jog_operation_button.pack(side="left")
        self.place(x=0, y=0, width=500, height=25)

    def open_port_config_window(self):
        self.port_window = tk.Toplevel()
        self.port_window.title("Port Configuration")
        self.port_window.geometry("600x220")
        self.port_frame = PortConfigurationFrame(self.port_window)

    def open_jog_operation_window(self):
        self.jog_window = tk.Toplevel()
        self.jog_window.title("Jog Operation")
        self.jog_window.geometry("600x700")
        self.jog_frame = JogOperationFrame(self.jog_window)

class PortConfigurationFrame(ttk.Frame):
    def __init__(self, container, app):
        super().__init__(container)
        self.app = app
        self.param_dict = {
            'Send Timeout': tk.IntVar(),
            'Receive Timeout': tk.IntVar(),
            'Port': tk.StringVar(),
            'Baud Rate': tk.IntVar(),
            'Data Bits': tk.IntVar(),
            'Parity': tk.StringVar(),
            'Stop Bits': tk.DoubleVar()
        }
        options = {'padx': 5, 'pady': 5}

        # Frame with default settings buttons:
        self.default_settings_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.default_settings_frame.grid(row=0, column=0, **options)

        # Add buttons to frame
        self.default_config_1 = tk.Button(self.default_settings_frame, text="Default 1",
                                          command=self.insert_default_settings)
        self.default_config_1.grid(row=0, column=0, **options)
        self.default_config_2 = tk.Button(self.default_settings_frame, text="Default 2",
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
class JogOperationFrame(tk.Frame):
    """
        Window for port configuration, here we have code to configure and enstablish com connection
    """


    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}
        # frame with jog parts
        self.default_settings_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.default_settings_frame.grid(row=0, column=0, **options)

        # Labels
        tk.Label(self.default_settings_frame, text="Waist").grid(row=0, column=0, **options)
        tk.Label(self.default_settings_frame, text="Shoulder").grid(row=1, column=0,  **options)
        tk.Label(self.default_settings_frame, text="Elbow").grid(row=2, column=0, **options)
        tk.Label(self.default_settings_frame, text="Twist").grid(row=3, column=0,  **options)
        tk.Label(self.default_settings_frame, text="Pitch").grid(row=4, column=0,  **options)
        tk.Label(self.default_settings_frame, text="Roll").grid(row=5, column=0,  **options)
        # Arrow buttons
        self.left_waist = tk.Button(self.default_settings_frame, text="🠸")
        self.left_waist.grid(row=0, column=1, **options)
        self.right_waist = tk.Button(self.default_settings_frame, text="🠺")
        self.right_waist.grid(row=0, column=2, **options)

        self.left_shoulder = tk.Button(self.default_settings_frame, text="🠸")
        self.left_shoulder.grid(row=1, column=1, **options)
        self.right_shoulder = tk.Button(self.default_settings_frame, text="🠺")
        self.right_shoulder.grid(row=1, column=2, **options)

        self.left_elbow = tk.Button(self.default_settings_frame, text="🠸")
        self.left_elbow.grid(row=2, column=1, **options)
        self.right_elbow = tk.Button(self.default_settings_frame, text="🠺")
        self.right_elbow.grid(row=2, column=2, **options)

        self.left_twist = tk.Button(self.default_settings_frame, text="🠸")
        self.left_twist.grid(row=3, column=1, **options)
        self.right_twist = tk.Button(self.default_settings_frame, text="🠺")
        self.right_twist.grid(row=3, column=2, **options)

        self.left_pitch = tk.Button(self.default_settings_frame, text="🠸")
        self.left_pitch.grid(row=4, column=1, **options)
        self.right_pitch = tk.Button(self.default_settings_frame, text="🠺")
        self.right_pitch.grid(row=4, column=2, **options)

        self.left_roll = tk.Button(self.default_settings_frame, text="🠸")
        self.left_roll.grid(row=5, column=1, **options)
        self.right_roll = tk.Button(self.default_settings_frame, text="🠺")
        self.right_roll.grid(row=5, column=2, **options)


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
        com_port = ComPort(**{
            'Port': self.param_dict['Port'].get(),
            'Baud Rate': self.param_dict['Baud Rate'].get(),
            'Data Bits': self.param_dict['Data Bits'].get(),
            'Parity': self.param_dict['Parity'].get(),
            'Stop Bits': self.param_dict['Stop Bits'].get(),
            'Send Timeout': self.param_dict['Send Timeout'].get(),
            'Read Timeout': self.param_dict['Receive Timeout'].get()
        })
        self.app.set_com_port(com_port)

    def on_disconnect(self):
        self.app.com_port.close()
        self.app.com_port = None


    def send_some_info(self):
        self.app.com_port.write(b'Hello')


class ToolBox(ttk.Frame):
    def __init__(self, container, app):
        super().__init__(container)
        self.app = app
        self.port_config_button = tk.Button(self, text="Configure port", command=self.open_port_config_window)
        self.port_config_button.pack(side="left")
        self.place(x=0, y=0, width=500, height=25)

    def open_port_config_window(self):
        self.port_window = tk.Toplevel()
        self.port_window.title("Port Configuration")
        self.port_window.geometry("600x220")
        self.port_config = PortConfigurationFrame(self.port_window, self.app)


class Wczytywanie_danych(ttk.Frame):
    """
        Toolbox in app, here will be fields and methods handling some config windows
    """
    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}
        # label for send
        tk.Label(self, text="Send:").grid(row=0, column=0)
        self.send_entry = tk.Entry(self)
        self.send_entry.grid(row=0, column=1)
        self.place(x=0, y=25, width=500, height=50)
        # buttons for send
        self.connect_button = tk.Button(self, text="Send")
        self.connect_button.grid(row=3, column=1)

class App(tk.Tk):
    """
        Main app class
    """
    def __init__(self):
        super().__init__()
        self.title('Roboty Przemyslowe')
        self.geometry('800x500')
        self.com_port = None
        ToolBox(self, self)

    def set_com_port(self, com_port):
        self.com_port = com_port
        self.geometry('500x300')
        # ToolBox
        ToolBox(self)
        Wczytywanie_danych(self)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
