import scipy.signal as signal
from scipy.fft import fft, fftfreq
import tkinter as tk
from tkinter import filedialog, ttk
import wave
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Model class
class Model:
    #Creates model instance
    def __init__(self):
        self.file_path = None
        self.sample_rate = None
        self.data = None

    #Retrieves vital information about a .wav file, including sample rate, number of samples,
    #and converts the file to mono from stereo if needed
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
    
    #Computes the highest resonant frequency
    def compute_resonant_frequency(self):
        #Perform FFT to get the frequency spectrum
        N = len(self.data)
        #Compute the FFT of the data
        yf = fft(self.data)
        xf = fftfreq(N, 1 / self.sample_rate)
        
        #Get the positive half of the spectrum
        half_n = N // 2
        xf = xf[:half_n]
        yf = yf[:half_n]
        
        #Compute the magnitude of the FFT
        magnitude = np.abs(yf)
        
        #Find the frequency with the highest magnitude (peak)
        resonant_frequency_index = np.argmax(magnitude)
        resonant_frequency = xf[resonant_frequency_index]
        
        return resonant_frequency
    
    #Isolates a specific band of frequencies, used for isolating between low, med, and high freqs.
    def filter_band(self, low_freq, high_freq):
        nyquist = 0.5 * self.sample_rate  # Nyquist frequency: minimum frequency that a signal can be sampled without error

        #Design the band-pass filter
        low = low_freq / nyquist
        high = high_freq / nyquist

        #Ensure valid filter design
        if low <= 0 or high >= 1 or low >= high:
            return np.zeros_like(self.data)  # Return silence for invalid filter params

        b, a = signal.butter(4, [low, high], btype='band')  # Order 4 Butterworth filter
        filtered_signal = signal.filtfilt(b, a, self.data)

        #Avoid division by zero when normalizing
        max_amplitude = np.max(np.abs(filtered_signal))
        if max_amplitude == 0:
            return np.zeros_like(filtered_signal)

        return filtered_signal / max_amplitude

    #Computes RT60 data for each band
    def compute_rt60(self, band_data):
        #Compute the magnitude of the band signal (envelope)
        envelope = np.abs(band_data)

        #Normalize the envelope
        envelope = envelope / np.max(envelope)

        #Generate time data
        time = np.linspace(0, len(envelope) / self.sample_rate, len(envelope))

        #Return time and envelope (decay data)
        return time, envelope
    
    #Subtracts the target RT60 (.5s) from all three band ranges, then finds the average between them
    def compute_rt60_diff(self, rt60_low, rt60_med, rt60_high):
        #Compute RT60 values for each band
        target_rt60 = .5
        
        #Calculate the difference from the target RT60 (0.5 seconds)
        diff_low = rt60_low - target_rt60
        diff_med = rt60_med - target_rt60
        diff_high = rt60_high - target_rt60
        
        return (diff_low + diff_med + diff_high) / 3