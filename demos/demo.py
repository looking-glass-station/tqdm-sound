from tqdm_sound import TqdmSound
import random
import time


if __name__ == "__main__":
    mt_list = my_list = [0] * 10

    sound_monitor = TqdmSound(theme="ryoji_ikeda", activity_mute_seconds=1, dynamic_settings_file=r"dynamic_settings.json")
    progress_one = sound_monitor.progress_bar(mt_list, desc="Processing", end_wait=1, ten_percent_ticks=True)
    for _ in progress_one:
        time.sleep(random.uniform(.2, .5))




