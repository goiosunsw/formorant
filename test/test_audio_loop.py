from audio_loop import AudioLoop
import argparse
from time import sleep

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

parser = argparse.ArgumentParser(add_help=False)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    'channels', type=int, default=[1], nargs='*', metavar='CHANNEL',
    help='input channels to plot (default: the first)')
parser.add_argument(
    '-i', '--in-device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-o', '--out-device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-b', '--blocksize', type=int, help='block size (in samples)')
parser.add_argument(
    '-r', '--samplerate', type=float, help='sampling rate of audio device')
parser.add_argument('--dtype', help='audio data type')
parser.add_argument('--latency', type=float, help='latency in seconds')
args = parser.parse_args()

al = AudioLoop(samplerate=args.samplerate,
               blocksize=args.blocksize)
al.start()
print("starting")
for ii in range(1,10):
    sleep(0.1)
    data = al.get_data()
    print(f"got data, shape {data.shape}")

print("stopping")
print(f"Blocks in queue: {al.q.qsize()}")
al.stop()
