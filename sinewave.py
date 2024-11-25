import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave(frequency=1, amplitude=1, phase_shift=0, duration=2, sample_rate=1000):
    """
    Plots a sine wave based on given parameters.

    Args:
    frequency (float): Frequency of the sine wave in Hz.
    amplitude (float): Amplitude of the sine wave.
    phase_shift (float): Phase shift of the sine wave in radians.
    duration (float): Duration of the sine wave in seconds.
    sample_rate (int): Number of samples per second for generating the sine wave.

    """
    # Time vector
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # Generate sine wave
    y = amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
    
    # Plot the sine wave
    plt.figure(figsize=(10, 4))
    plt.plot(t, y)
    plt.title(f"Sine Wave: Frequency={frequency}Hz, Amplitude={amplitude}, Phase Shift={phase_shift} rad")
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

# Example usage:
if __name__ == "__main__":
    plot_sine_wave(frequency=10, amplitude=1, phase_shift=0, duration=2, sample_rate=1000)
