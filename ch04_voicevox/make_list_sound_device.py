import os
import sounddevice as sd

file = os.path.join(os.path.dirname(__file__), "sound_device.txt")
with open(file, "w", encoding="utf-8") as f:
    f.write(str(sd.query_devices()))
