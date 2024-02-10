import sys
import sounddevice as sd
import numpy as np
import queue

class AudioLoop(object):
    def __init__(self, samplerate=None,
                 channels=[1], 
                 in_device=None, out_device=None,
                 blocksize=None, dtype=None,
                 latency=None):
        self.stream = sd.Stream(device=(in_device, out_device),
                                channels=max(channels),
                                samplerate=samplerate,
                                blocksize=blocksize,
                                dtype=dtype,
                                latency=latency,
                                callback=self.audio_callback)
        self.mapping = [c-1 for c in channels]
        self.q = queue.Queue()

    def audio_callback(self, indata, outdata, frames, time, status):
        if status:
            print("AUDIO ERROR")
            print(status, file=sys.stderr)
        self.q.put(indata[:,self.mapping])
        outdata[:] = np.random.rand(*indata.shape)

    def start(self):
        self.stream.start()

    def stop(self):
        self.stream.stop()

    def get_data(self):
        status = 0
        blocks = []
        while True:
            try:
                blocks.append(self.q.get_nowait())
            except queue.Empty:
                break
        return np.concatenate(blocks)