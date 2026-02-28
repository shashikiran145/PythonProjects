import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

TARGET_IP = "172.18.1.91"
TARGET_PORT = 5001

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Sending audio... press CTRL+C to stop")
try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        sock.sendto(data, (TARGET_IP, TARGET_PORT))
except KeyboardInterrupt:
    print("\nStopped")
except OSError as e:
    print(f"\nAudio/socket error: {e}")
finally:
    stream.stop_stream()
    stream.close()       # was missing — frees the audio device
    p.terminate()
    sock.close()