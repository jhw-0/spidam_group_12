from tkinter import filedialog

# Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.select_button.config(command=self.select_file)

    def select_file(self):
        # Prompts user to select a file. File type can be
        # .wav, .mp3, .flac, or .ogg
        file_path = filedialog.askopenfilename(
            title="Select an audio File",
            filetypes=(("Audio Files", "*.wav *.mp3 *.flac *.ogg"), ("All Files", "*.*"))
        )
        # Executes everything in this if statement once file is selected
        if file_path:
            self.model.load_wav(file_path)
            time = len(self.model.data) / self.model.sample_rate
            resonant_frequency = self.model.compute_resonant_frequency()

            # Filter bands
            low_band = self.model.filter_band(20, 200)
            mid_band = self.model.filter_band(200, 2000)
            high_band = self.model.filter_band(2000, 20000)

            # Compute RT60 and time for each band
            time_low, rt60_low = self.model.compute_rt60(low_band)
            time_mid, rt60_mid = self.model.compute_rt60(mid_band)
            time_high, rt60_high = self.model.compute_rt60(high_band)

            rt60_diff = self.model.compute_rt60_diff(rt60_low, rt60_mid, rt60_high)
            print(rt60_diff)

            # Updates all necessary information, including time,
            # highest freq., and displays both graphs
            self.view.update_time(time)
            self.view.update_resonant_frequency(resonant_frequency)
            self.view.update_rt60_difference(rt60_diff)
            self.view.update_waveform_graph(self.model.sample_rate, self.model.data, time)
            self.view.update_rt60_low_graph(time_low, rt60_low)
            self.view.update_rt60_med_graph(time_mid, rt60_mid)
            self.view.update_rt60_high_graph(time_high, rt60_high)
            self.view.update_rt60_all_graph(time_low, rt60_low, time_mid, rt60_mid, time_high, rt60_high)