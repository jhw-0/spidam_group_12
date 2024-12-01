import tkinter as tk
from tkinter import filedialog, ttk
import wave
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# View
class View:
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.select_button = ttk.Button(self.frame, text="Load Audio File")
        self.select_button.pack(padx=5,pady=10)

        self.info_label = ttk.Label(self.frame, text="Length of Clip: Not Loaded", font=("Arial", 12))
        self.info_label.pack(pady=5)

        self.canvas_frame = ttk.Frame(self.frame)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.figure = Figure(figsize=(8, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Waveform")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Amplitude")
        self.canvas = None

    def update_graph(self, sample_rate, data, time):
        self.info_label.config(text=f"Length of Clip: {time:.2f} seconds")

        self.ax.clear()
        self.ax.set_title("Waveform")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Amplitude")
        time = np.linspace(0, len(data) / sample_rate, num=len(data))
        self.ax.plot(time, data, linewidth=0.5)
        self.ax.set_xlim(0, time[-1])

        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)