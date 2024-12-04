import scipy.signal as signal
from scipy.fft import fft, fftfreq
import wave
import numpy as np
from typing import Tuple, Any
from numpy.typing import NDArray
import pydub
from pathlib import Path

# Model class
class Model:

    def __init__(self):
        self.file_path: Path | None = None
        self.audio_file: pydub.AudioSegment | None = None
        self.sample_rate: int | None = None
        self.data: NDArray[Any] | None = None

    def set_file_path(self, file_path : str) -> None:
        self.file_path = Path(file_path) 

    def load_audio_file(self) -> None:
        # Setting audio_file
        self.audio_file = pydub.AudioSegment.from_file(
            self.file_path,
            format=self.file_path.suffix[1:] # `[1:]` to remove the '.'
        )
        # Below, processing audio_file to be usable
        # Export to wav conditionally
        if not self.check_if_wav() or self.check_meta():
            self.export_to_wav()
        # Convert to one channel audio
        if not self.check_if_one_channel():
            self.convert_to_one_channel()

    def check_if_wav(self) -> bool:
        return self.file_path.suffix == '.wav'
    
    def export_to_wav(self) -> str:
        # resetting the _audio_file attribute
        self.audio_file.export(
            # caches the audio file next to the old one on the file sys
            destination := self.file_path.with_suffix('.wav'),
            format='wav'
        )
        # resetting the file_path attribute
        self.file_path = destination
        # resetting the audio_file attribute
        self.audio_file = pydub.AudioSegment.from_file(
            self.file_path,
            format='wav'
        )

    def check_meta(self) -> bool:
        return bool(pydub.utils.mediainfo(str(self.audio_file)).get('TAG'))
    
    def check_if_one_channel(self) -> bool:
        print(self.audio_file)
        print(type(self.audio_file))
        return self.audio_file.channels == 1

    def convert_to_one_channel(self) -> None:
        # resetting the _audio_file attribute
        self.audio_file = self.audio_file.set_channels(1)

    # Retrieves vital information about a .wav file, including sample rate,
    # and number of samples.
    def load_wav(self) -> None:
        self.load_audio_file()
        with wave.open(str(self.file_path), 'rb') as wav_file:
            self.sample_rate: int = wav_file.getframerate()
            n_frames: int = wav_file.getnframes()
            data: bytes = wav_file.readframes(n_frames)
            self.data: NDArray[Any] = np.frombuffer(data, dtype=np.int16)
    
    # Computes the highest resonant frequency
    def compute_resonant_frequency(self) -> np.float64:
        # Perform FFT to get the frequency spectrum
        N: int = len(self.data)
        # Compute the FFT of the data
        yf = fft(self.data)
        xf = fftfreq(N, 1 / self.sample_rate)
        
        # Get the positive half of the spectrum
        half_n = N // 2
        xf = xf[:half_n]
        yf = yf[:half_n]
        
        # Compute the magnitude of the FFT
        magnitude = np.abs(yf)
        
        # Find the frequency with the highest magnitude (peak)
        resonant_frequency_index = np.argmax(magnitude)
        resonant_frequency = xf[resonant_frequency_index]
        return resonant_frequency
    
    # Isolates a specific band of frequencies, used for isolating between low,
    # med, and high freqs.
    def filter_band(self, low_freq, high_freq) -> NDArray[Any]:
        # Nyquist frequency: minimum frequency that a signal
        # can be sampled without error
        nyquist = 0.5 * self.sample_rate  
        # Design the band-pass filter
        low = low_freq / nyquist
        high = high_freq / nyquist

        # Ensure valid filter design
        if low <= 0 or high >= 1 or low >= high:
            # Return silence for invalid filter params
            return np.zeros_like(self.data)

        # Order 4 Butterworth filter
        b, a = signal.butter(4, [low, high], btype='band')
        filtered_signal = signal.filtfilt(b, a, self.data)

        #Avoid division by zero when normalizing
        max_amplitude = np.max(np.abs(filtered_signal))
        if max_amplitude == 0:
            return np.zeros_like(filtered_signal)

        return filtered_signal / max_amplitude

    # Computes RT60 data for each band
    def compute_rt60(self, band_data) -> Tuple[NDArray[Any], NDArray[Any]]:
        # Compute the magnitude of the band signal (envelope)
        envelope = np.abs(band_data)

        # Normalize the envelope
        envelope = envelope / np.max(envelope)

        # Generate time data
        time = np.linspace(0, len(envelope) / self.sample_rate, len(envelope))

        # Return time and envelope (decay data)
        return time, envelope
    
    # Subtracts the target RT60 (.5s) from all three band ranges,
    # then finds the average between them
    def compute_rt60_diff(self, rt60_low, rt60_med, rt60_high):
        # Compute RT60 values for each band
        target_rt60 = .5
        
        # Calculate the difference from the target RT60 (0.5 seconds)
        diff_low = rt60_low - target_rt60
        diff_med = rt60_med - target_rt60
        diff_high = rt60_high - target_rt60
        
        return (diff_low + diff_med + diff_high) / 3