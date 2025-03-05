from asr.asr_module import record_audio, save_audio_to_file, transcribe_audio
from tts.tts_module import text_to_speech
import os
import sounddevice as sd
import soundfile as sf

def play_audio(file_path):
    data, fs = sf.read(file_path, dtype='float32')
    sd.play(data, fs)
    sd.wait()

def conversation_flow():
    print("Please speak now...")
    # Record and transcribe audio
    audio = record_audio(duration=5)
    audio_file = save_audio_to_file(audio)
    transcription = transcribe_audio(audio_file)
    print("You said:", transcription)
    os.remove(audio_file)

    # Create a simple response (e.g., echoing)
    response = f"You said: {transcription}"
    print("Response:", response)
    tts_audio_file = text_to_speech(response)
    play_audio(tts_audio_file)

if __name__ == "__main__":
    conversation_flow()
