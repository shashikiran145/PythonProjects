import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
channels = 1
RATE = 44100

TARGET_IP = "172.18.1.91"
TARGET_PORT = 5001

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=channels, rate=RATE, input=True, frames_per_buffer=CHUNK)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Sending audio.. press CTRL+C to stop")
try:
    while True:
        data = stream.read(CHUNK)
        sock.sendto(data, (TARGET_IP, TARGET_PORT))
except KeyboardInterrupt:
    print("\nStopped")
    stream.stop_stream()
    stream.stop_stream()
    p.terminate()
    sock.close()