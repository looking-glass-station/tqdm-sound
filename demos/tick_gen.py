import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt


def generate_tick(sample_rate=44100, duration=0.02):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    freq = 1000  # Fixed frequency for clock tick
    tick_wave = np.exp(-20 * t) * np.sin(2 * np.pi * freq * t)  # Damped sine wave

    # Randomly adjust left/right dominance
    left_gain = np.random.uniform(0.7, 1.0)
    right_gain = np.random.uniform(0.7, 1.0)

    stereo_tick = np.column_stack((tick_wave * left_gain, tick_wave * right_gain))
    return stereo_tick


def save_ticks(filename="clock_ticks.wav", num_ticks=10, sample_rate=44100, spacing=1.0):
    silence = np.zeros((int(sample_rate * spacing), 2))
    ticks = []

    for _ in range(num_ticks):
        ticks.append(generate_tick(sample_rate))
        ticks.append(silence)

    full_wave = np.vstack(ticks) * 32767  # Scale for int16 format
    full_wave = full_wave.astype(np.int16)

    wav.write(filename, sample_rate, full_wave)
    print(f"Saved {num_ticks} clock ticks to {filename}")


# Generate and save 10 clock ticks
save_ticks()
