import queue
import sys

import sounddevice as sd
import soundfile as sf



q = queue.Queue()


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

# print(sd.query_devices())
# exit(0)
sd.default.device[0] = 31

# soundfile expects an int, sounddevice provides a float:
samplerate = 48000
channels = 1
# Make sure the file is opened before recording anything:
with sf.SoundFile("test.wav", mode='w', samplerate=samplerate,channels=channels) as file:
    with sd.InputStream(samplerate=samplerate, device=None,channels=channels, callback=callback):
        print('#' * 80)
        print('press Ctrl+C to stop the recording')
        print('#' * 80)
        while True:
            file.write(q.get())






