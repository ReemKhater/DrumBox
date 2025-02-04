import os
import wave
import pyaudio

# Mapping des sons aux boutons
SOUNDS = {
    1: "data/sound1.wav",
    2: "data/sound2.wav",
    3: "data/sound3.wav",
    4: "data/sound4.wav",
    5: "data/sound5.wav",
    6: "data/sound6.wav"
}

def play_sound(button):
    sound_file = SOUNDS.get(button)
    if sound_file and os.path.exists(sound_file):
        play_wave_file(sound_file)
    else:
        print(f"Fichier son pour le bouton {button} introuvable.")

def play_wave_file(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()
