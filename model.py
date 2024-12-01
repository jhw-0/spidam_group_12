import tkinter as tk
from tkinter import filedialog, ttk
import wave
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Model
class Model:
    def __init__(self):
        self.file_path = None
        self.sample_rate = None
        self.data = None

    def load_wav(self, file_path):
        self.file_path = file_path
        with wave.open(file_path, 'rb') as wav_file:
            self.sample_rate = wav_file.getframerate()
            n_frames = wav_file.getnframes()
            n_channels = wav_file.getnchannels()
            data = wav_file.readframes(n_frames)
            self.data = np.frombuffer(data, dtype=np.int16)
            if n_channels == 2:  # Stereo to mono
                self.data = self.data[::2]