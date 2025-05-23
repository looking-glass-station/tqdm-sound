from tqdm_sound import TqdmSound
import random
import time

if __name__ == "__main__":
    sound_monitor = TqdmSound(theme="ryoji_ikeda", activity_mute_seconds=5)

    my_list = [0] * 50
    progress_one = sound_monitor.progress_bar(my_list, desc="Processing", end_wait=1, ten_percent_ticks=True)
    for _ in progress_one:
        time.sleep(random.uniform(.2, .5))

    sound_monitor.play_final_end_tone(80)

    sound_monitor.close()


