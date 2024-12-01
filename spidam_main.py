from model import Model
from view import View
from controller import Controller

import tkinter as tk
from tkinter import filedialog, ttk
import wave
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Main Application
def main():
    root = tk.Tk()
    root.title("Waveform Viewer")
    root.geometry("800x600")

    model = Model()
    view = View(root)
    controller = Controller(model, view)

    root.mainloop()

if __name__ == "__main__":
    main()