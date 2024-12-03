import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# View class
class View:

    def __init__(self, root):
        self.root = root

        # Creates a frame for the load, time, and highest frequency labels
        top_frame = ttk.Frame(root)
        top_frame.pack(fill=tk.X, pady=10)

        # Create the "Load Audio File" button
        self.select_button = tk.Button(top_frame, text="Load Audio File")
        self.select_button.pack(side=tk.LEFT, padx=10)

        # Creates a tabbed interface for cycling between graphs
        notebook = ttk.Notebook(root)
        notebook.pack(fill=tk.BOTH, expand=True)
        # Create a frame for each tab
        waveform_frame = ttk.Frame(notebook)
        rt60_low_frame = ttk.Frame(notebook)
        rt60_med_frame = ttk.Frame(notebook)
        rt60_high_frame = ttk.Frame(notebook)
        rt60_all_frame = ttk.Frame(notebook)
        # Add named tabs to the notebook
        notebook.add(waveform_frame, text="Waveform")
        notebook.add(rt60_low_frame, text="RT60 Low")
        notebook.add(rt60_med_frame, text="RT60 Med")
        notebook.add(rt60_high_frame, text="RT60 High")
        notebook.add(rt60_all_frame, text="RT60 All")

        # Creates the "Time: ___s" label
        self.time_label = ttk.Label(
            top_frame,
            text="Time: Not Calculated"
        )
        self.time_label.pack(side=tk.LEFT, padx=10)
        
        # Creates the "Highest Resonant Frequency: ___Hz" label
        self.resonant_label = ttk.Label(
            top_frame,
            text="Highest Resonant Frequency: Not Calculated"
        )
        self.resonant_label.pack(side=tk.LEFT, padx=10)

        # Creates the "Difference: ___s" label
        self.difference_label = ttk.Label(
            top_frame,
            text="Difference: Not Calculated"
        )
        self.difference_label.pack(side=tk.LEFT, padx=10)
        
        # Initialize figure for waveform graph
        figure_waveform = Figure(figsize=(10, 7), dpi=100)
        self.ax_waveform = figure_waveform.add_subplot(111)
        self.ax_waveform.set_title("Waveform")
        self.ax_waveform.set_xlabel("Time (s)")
        self.ax_waveform.set_ylabel("Amplitude")

        # Helper function that initializes figures
        def set_ax_rt60(
            figure: Figure,
            decay_time_type: str
        ) -> Axes:
            ax: Axes = figure.add_subplot(111)
            ax.set_title(f"{decay_time_type} RT60 Decay Time")
            ax.set_xlabel("Frequency Band")
            ax.set_ylabel("RT60 (s)")
            return ax
        
        # Initialize figure for remaining graphs
        figure_rt60_low = Figure(figsize=(10, 7), dpi=100)
        figure_rt60_med = Figure(figsize=(10, 7), dpi=100)
        figure_rt60_high = Figure(figsize=(10, 7), dpi=100)
        figure_rt60_all = Figure(figsize=(10, 7), dpi=100)
        self.ax_rt60_low = set_ax_rt60(figure_rt60_low, "Low")
        self.ax_rt60_med = set_ax_rt60(figure_rt60_med, "Medium")
        self.ax_rt60_high = set_ax_rt60(figure_rt60_high, "High")
        self.ax_rt60_all = set_ax_rt60(figure_rt60_all, "All")

        # Helper function that creates canvases
        def create_canvas(
            figure: Figure,
            master_frame
        ) -> FigureCanvasTkAgg:
            # Create canvas for corresponding figure and frame
            canvas = FigureCanvasTkAgg(
                figure,
                master=master_frame
            )
            # Pack the canvas
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            return canvas
        
        # Create separate canvases for each graph
        self.canvas_waveform = create_canvas(
            figure=figure_waveform,
            master_frame=waveform_frame
        )
        self.canvas_rt60_low = create_canvas(
            figure=figure_rt60_low,
            master_frame=rt60_low_frame
        )
        self.canvas_rt60_med = create_canvas(
            figure=figure_rt60_med,
            master_frame=rt60_med_frame
        )
        self.canvas_rt60_high = create_canvas(
            figure=figure_rt60_high,
            master_frame=rt60_high_frame
        )
        self.canvas_rt60_all = create_canvas(
            figure=figure_rt60_all,
            master_frame=rt60_all_frame
        )

    # Updates the time label when a file is selected
    def update_time(self, time):
        self.time_label.config(text=f"Time: {time:.2f}s")

    # Updates the resonant frequency label when a file is selected
    def update_resonant_frequency(self, resonant_frequency):
        # Update the label with the highest resonant frequency
        self.resonant_label.config(
            text=f"Highest Resonant Frequency: {resonant_frequency:.2f} Hz"
        )
    
    def update_rt60_difference(self, rt60_diff):
        self.difference_label.config(text=f"Difference: {rt60_diff}s")

    # Displays the waveform graph when a file is selected
    def update_waveform_graph(self, sample_rate, data, time):
        time = np.linspace(0, len(data) / sample_rate, num=len(data))
        self.ax_waveform.clear()
        self.ax_waveform.set_title("Waveform")
        self.ax_waveform.set_xlabel("Time (s)")
        self.ax_waveform.set_ylabel("Amplitude")
        self.ax_waveform.plot(time, data, linewidth=0.5)
        self.ax_waveform.set_xlim(0, time[-1])
        # Redraw the waveform canvas
        self.canvas_waveform.draw()

    # Displays the low frequency RT60 decay graph when a file is selected
    def update_rt60_low_graph(self, time_low, rt60_low):
        self.ax_rt60_low.clear()
        self.ax_rt60_low.set_title("Low RT60 Decay Time")
        self.ax_rt60_low.set_xlabel("Frequency Band")
        self.ax_rt60_low.set_ylabel("RT60 (s)")
        self.ax_rt60_low.plot(
            time_low,
            rt60_low,
            label="Low RT60",
            color="blue"
        )
        # Redraw the low RT60 decay canvas
        self.canvas_rt60_low.draw()
    
    # Displays the medium frequency RT60 decay graph when a file is selected
    def update_rt60_med_graph(self, time_med, rt60_med):
        self.ax_rt60_med.clear()
        self.ax_rt60_med.set_title("Medium RT60 Decay Time")
        self.ax_rt60_med.set_xlabel("Frequency Band")
        self.ax_rt60_med.set_ylabel("RT60 (s)")
        self.ax_rt60_med.plot(
            time_med, 
            rt60_med,
            label="Medium RT60",
            color="green"
        )
        # Redraw the medium RT60 decay canvas
        self.canvas_rt60_med.draw()

    # Displays the high frequency RT60 decay graph when a file is selected
    def update_rt60_high_graph(self, time_high, rt60_high):
        self.ax_rt60_high.clear()
        self.ax_rt60_high.set_title("High RT60 Decay Time")
        self.ax_rt60_high.set_xlabel("Frequency Band")
        self.ax_rt60_high.set_ylabel("RT60 (s)")
        self.ax_rt60_high.plot(
            time_high,
            rt60_high,
            label="High RT60",
            color="red"
        )
        # Redraw the high RT60 decay canvas
        self.canvas_rt60_high.draw()

    # Displays all three graphs simultaneously
    def update_rt60_all_graph(
        self,
        time_low,
        rt60_low,
        time_med,
        rt60_med,
        time_high,
        rt60_high
    ) -> None:
        self.ax_rt60_all.clear()
        self.ax_rt60_all.set_title("All RT60 Decay Time")
        self.ax_rt60_all.set_xlabel("Frequency Band")
        self.ax_rt60_all.set_ylabel("RT60 (s)")
        # Draws all plots onto the same graph
        self.ax_rt60_all.plot(
            time_low,
            rt60_low,
            label="Low RT60",
            color="blue"
        )
        self.ax_rt60_all.plot(
            time_med, rt60_med,
            label="Medium RT60",
            color="green"
        )
        self.ax_rt60_all.plot(
            time_high,
            rt60_high,
            label="High RT60",
            color="red"
        )
        self.canvas_rt60_all.draw()