import pyaudio
import wave
import pynput.mouse

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
THRESHOLD = 1500  

# Initializing PyAudio
p = pyaudio.PyAudio()

# Ouverture du flux audio
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

noise_detected = False

while True:
    # Reading Sound
    data = stream.read(CHUNK)
    data_int = wave.struct.unpack("%dh"%(len(data)/2), data)
    amplitude = max(data_int)
    
    if amplitude > THRESHOLD:
        print("Sound amplitude is : ", amplitude)
        mouse = pynput.mouse.Controller()
        mouse.press(pynput.mouse.Button.left)
        noise_detected = True
    elif noise_detected:
        mouse.release(pynput.mouse.Button.left)
        noise_detected = False

# Fermeture du flux audio
stream.stop_stream()
stream.close()
p.terminate()
