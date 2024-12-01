import model
import tkinter as tk
from tkinter import filedialog, ttk
import wave
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.select_button.config(command=self.select_file)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a WAV File",
            filetypes=(("WAV Files", "*.wav"), ("All Files", "*.*"))
        )
        if file_path:
            self.model.load_wav(file_path)
            time = len(self.model.data) / self.model.sample_rate
            self.view.update_graph(self.model.sample_rate, self.model.data, time)