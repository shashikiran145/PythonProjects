# This is a trial project

import socket
import pyaudio
import threading


CHUNK = 1024
CHANNELS = 1
FORMAT = pyaudio.paInt16
RATE = 44100

TARGET_IP = "127.0.0.1"
TARGET_PORT = 6001
LISTEN_PORT = 6002

p = pyaudio.PyAudio()


def send_audio():
    stream = p.open(rate=RATE, channels=CHANNELS, input=True, frames_per_buffer=CHUNK, format=FORMAT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Sending audio.. press CTRL+C to terminate")
    while True:
        try:
            data = stream.read(num_frames=CHUNK, exception_on_overflow=False)
            sock.sendto(data, (TARGET_IP, TARGET_PORT))
        except Exception as e:
            print(f"[Send error] {e}")
            break


def receive_audio():
    stream = p.open(rate=RATE, channels=CHANNELS, output=True, frames_per_buffer=CHUNK, format=FORMAT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", LISTEN_PORT))
    print(f"Listening on port {LISTEN_PORT}")
    while True:
        try:
            data, _ = sock.recvfrom(CHUNK*2)
            stream.write(data)
        except Exception as e:
            print(f"Error message: {e}")
            break


t1 = threading.Thread(target=send_audio)
t2 = threading.Thread(target=receive_audio)

t1.start()
t2.start()



