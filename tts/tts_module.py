from TTS.api import TTS

def text_to_speech(text, model_name="tts_models/en/ljspeech/tacotron2-DDC"):
    # Initialize TTS with a pre-trained model
    tts = TTS(model_name)
    # Save the generated speech to an audio file
    output_path = "output.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path

if __name__ == "__main__":
    response = "Hello, this is a test of Mozilla TTS."
    audio_file = text_to_speech(response)
    print("Audio saved to:", audio_file)
    # Optionally, use an audio playback library to play the file
