# -*- coding: utf-8 -*-
import pyaudio
import wave
import numpy


def RecordAudioInFile(CHANNELS,RECORD_SECONDS, WAVE_OUTPUT_FILENAME = "mfcc.wav"):
    p = pyaudio.PyAudio()
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def GetRecordAudio(CHANNELS,RECORD_SECONDS):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    return numpy.fromstring(numpy.asarray(frames), dtype=numpy.int16)


