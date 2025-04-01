from tqdm_sound import TqdmSound
import random
import time

# Example usage:
if __name__ == "__main__":
    sound_monitor = TqdmSound(theme="ryoji_ikeda", activity_mute_seconds=1)

    my_list = [0] * 50
    progress_one = sound_monitor.progress_bar(my_list, desc="Processing", end_wait=1, ten_percent_ticks=True)
    for _ in progress_one:
        time.sleep(random.uniform(.2, .5))

    progress_two = sound_monitor.progress_bar(range(10), desc="Processing two", background_volume=50, volume=100)
    for _ in progress_two:
        time.sleep(random.uniform(.1, .2))

    sound_monitor.play_final_end_tone(80)
    sound_monitor.play_sound_file('program_end_tone.wav', 50)

    sound_monitor.close()  # Shutdown the global activity monitor when all progress bars are done.


