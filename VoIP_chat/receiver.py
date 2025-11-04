import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 5001

p = pyaudio.PyAudio()
stream = p.open(rate=RATE, channels=CHANNELS, format=FORMAT, frames_per_buffer=CHUNK, output=True)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_IP, LISTEN_PORT))

print("Listening for audio.. Press CTRL+C to stop")

try:
    while True:
        data, _ = sock.recvfrom(CHUNK*2)
        stream.write(data)
except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    p.terminate()
    sock.close()