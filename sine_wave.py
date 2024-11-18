import math
import matplotlib
import numpy

# import aliases
import matplotlib.pyplot as plt

def sine_wave_function(
        t,
        frequency,
        velocity,
        amplitude,
        x_displacement
    ):
    wavelength = velocity / frequency
    k = (2 * math.pi) / wavelength
    x_wavefront = velocity * t
    x_d = x_wavefront - x_displacement
    y = numpy.zeros_like(t)
    condition = x_wavefront >= x_displacement
    y[condition] = numpy.sin(k * x_d[condition]) * amplitude
    return y

def display_single_sine_wave(
        frequency,
        velocity,  
        amplitude,
        x_displacement
    ):
    ts = numpy.linspace(0.0, 1 / frequency, 100)
    ys = sine_wave_function(ts, frequency, velocity, amplitude, x_displacement)
    plt.plot(ts, ys)
    plt.title(
        f'Sine Wave - '
        f'f: {frequency} Hz, '
        f'v: {velocity} m/s, '
        f'A: {amplitude} m, '
        f'd: {x_displacement} m'
    )
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude [m]")
    plt.grid(True)
    plt.show()

if "__main__" == __name__:
    display_single_sine_wave(1500, 348, 1.5 * 10**(-9), 0.1)
    