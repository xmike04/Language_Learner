import whisper
import sounddevice as sd
import numpy as np
import tempfile
import os

def record_audio(duration=5, fs=16000):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    return np.squeeze(audio)

def save_audio_to_file(audio, fs=16000):
    import soundfile as sf
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    sf.write(temp_file.name, audio, fs)
    return temp_file.name

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result['text']

if __name__ == "__main__":
    audio = record_audio(duration=5)
    audio_file = save_audio_to_file(audio)
    transcription = transcribe_audio(audio_file)
    print("Transcription:", transcription)
    os.remove(audio_file)  # Clean up temporary file
