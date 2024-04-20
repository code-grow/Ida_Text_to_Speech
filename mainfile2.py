import pyttsx3

def main():
    converter = pyttsx3.init()
    engine = pyttsx3.init()

    #voices
    voices = engine.getProperty('voices')
    
    #choosing between different voices: male/female
    print("Available voices: ")
    for idx, voice in enumerate(voices):
        print(f"{idx + 1}. {voice.name}")
    voice_choice = int(input("Enter 1 for male voice or 2 for female voice: "))
    selected_voice = voices[voice_choice - 1]
    engine.setProperty('voice', selected_voice.id)
    


    #language selection
    print("Select a language:\n1. English (en)\n2. French (fr)\n3. German (de)\n4. Spanish (es)\n5. Italian (it)\n6. Romanian (ro)")


    lang_choice = input("Enter the language number (1 /2 /3 /4 /5 /6): ")
    if lang_choice == "1":  #english
        engine.setProperty("voice", "com.apple.speech.synthesis.voice.Alex")
    elif lang_choice == "2":#french
        engine.setProperty("voice", "com.apple.speech.synthesis.voice.Thomas")
    elif lang_choice == "3":#german
        engine.setProperty("voice", "com.apple.speech.synthesis.voice.Mark")
    elif lang_choice == "4":#spanish
        engine.setProperty("voice", "com.apple.speech.synthesis.voice.Monica")
    elif lang_choice == "5":#italian
        engine.setProperty("voice", "com.apple.speech.synthesis.voice.Alice")
    elif lang_choice == "6":#romanian
        engine.setProperty("voice", "com.apple.speech.synthesis.voice.Ioana")
    else:
        print("Invalid language choice. Using default (English).")

    #rate
    rate = float(input("Enter the desired speed of speech (the lower, the slower)-( 145 recommended ): "))
    engine.setProperty('rate', rate)  #Speed of speech -  the lower the number, the slower - the bigger the number, the faster

    #volume
    volume = float(input("Enter the desired volume (0.0 to 1.0) - (0.9 recommended): "))
    engine.setProperty('volume', volume)  #Volume(0.0 to 1.0)

    text = input("Enter the text you want to convert to speech: ")
    file_title = input("Enter the desired file title (without extension): ")
    playoption = int(input("Do you want to play the audio?\n(once it starts, you can not stop it)\n1-YES\t2-NO\nYour choice (type the number): "))


    engine.runAndWait()

    try:
        engine.save_to_file(text, f"{file_title}.mp3")
        engine.runAndWait()
        print(f"Audio file saved as {file_title}.mp3")
    except Exception as e:
        print(f"Error saving audio file: {e}")

    if playoption == 1: engine.say(text)#play at the end, because we want to play right after the audio was generated


if __name__ == "__main__":
    main()

#to transform from a text file into .mp3