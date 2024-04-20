import pyttsx3

engine = pyttsx3.init()

def text_to_speech(text, audio_file):
    
    engine.setProperty('rate', 145)  #Speed of speech-the lower the number the slower
    engine.setProperty('volume', 0.9)  #Volume(0.0 to 1.0)

    engine.save_to_file(text, f"{audio_file}.mp3")
    engine.runAndWait()

# text = "This is an announcement!"
text_input = input("Enter the text you want to convert to speech: ")
#audio_file = "speech_output.mp3"
audio_file = input("Enter the desired filename(without extension): ")
text_to_speech(text_input, audio_file)

print(f"The text has been converted to speech and saved as {audio_file}.mp3")
