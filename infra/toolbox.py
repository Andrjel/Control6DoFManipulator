import tkinter as tk
from tkinter import ttk
from infra.com_configuration_frame import PortConfigurationFrame
from infra.jog_operation_frame import JogOperationFrame
from infra.xyz_frame import XYZFrame


class ToolBox(ttk.Frame):
    """
        Toolbox in app, here will be fields and methods handling some config windows
    """
    def __init__(self, container, app):
        super().__init__(container)
        self.app = app
        # button for openning com port config
        self.toolbox_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        self.toolbox_frame.grid(row=0, column=0)
        self.port_config_button = tk.Button(self.toolbox_frame, text="Configure port",
                                            command=self.open_port_config_window)
        self.port_config_button.pack(side="left")
        # button for openning jog operation window
        self.jog_operation_button = tk.Button(self.toolbox_frame, text="Jog Operation",
                                              command=self.open_jog_operation_window)
        self.jog_operation_button.pack(side="left")

        # button for openning XYZ operation window
        self.XYZ_operation_button = tk.Button(self.toolbox_frame, text="XYZ Operation",
                                              command=self.open_XYZ_operation_window)
        self.XYZ_operation_button.pack(side="left")
        self.grid(row=0, column=0)

    def open_port_config_window(self):
        self.port_window = tk.Toplevel()
        self.port_window.title("Port Configuration")
        self.port_window.geometry("600x220")
        self.port_frame = PortConfigurationFrame(self.port_window, self.app)

    def open_jog_operation_window(self):
        self.jog_window = tk.Toplevel()
        self.jog_window.title("Jog Operation")
        self.jog_window.geometry("260x460")
        self.jog_window.resizable(False, False)
        self.jog_frame = JogOperationFrame(self.jog_window, self.app)

    def open_XYZ_operation_window(self):
        self.xyz_window = tk.Toplevel()
        self.xyz_window.title("XYZ Operation")
        self.xyz_window.geometry("600x460")
        self.xyz_window.resizable(False, False)
        self.xyz_frame = XYZFrame(self.xyz_window, self.app)
