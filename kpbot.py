import speech_recognition as sr
recognizer = sr.Recognizer()

#function for speech to text recognition
import speech_recognition as sr
import requests
import io  # For in-memory file handling

recognizer = sr.Recognizer()
mic_index = 0  # Change this if needed

while True:
    command = input("Type 'listen' to start recording or 'exit' to exit: ").strip().lower()

    if command == "listen":
        with sr.Microphone(device_index=mic_index) as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.energy_threshold = 300  
            recognizer.dynamic_energy_threshold = True
            recognizer.adjust_for_ambient_noise(source, duration=1)

            print("Listening... Speak now!")

            try:
                # Listen until user manually stops
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)

                stop_command = input("Type 'stop' to process your command: ").strip().lower()
                if stop_command == "stop":
                    print("Processing speech-to-text...")

                    # Send directly to API without saving
                    files = {
                        'file': ('command.wav', io.BytesIO(audio.get_wav_data()), 'audio/wav'),
                        'language': (None, 'english'),
                    }

                    response = requests.post('https://asr.iitm.ac.in/internal/asr/decode', files=files)

                    if response.status_code == 200:
                        result = response.json()
                        transcript = result.get("transcript", "")  # Extract only transcript
                        print("\n🎙️ **Transcribed Text:**", transcript)  # Print transcript directly
                    else:
                        print("Error:", response.text)

                    break  # Exit after processing one command

            except sr.WaitTimeoutError:
                print("No speech detected. Try again.")

    elif command == "exit":
        print("Exiting program...")
        break

    else:
        print("Invalid command! Type 'listen' to start recording or 'exit' to quit.")

import spacy
from spacy.matcher import PhraseMatcher

def custom_location_extractor(text):
    nlp=spacy.load("en_core_web_md")
    doc=nlp(text)

    custom_locations=["bakery", "chaat counter", "fast food counter","bill counter", "kitchen","sandwich counter","juice counter", "table one","table two",
                      "table three","table four","table five","table six","table seven",
                      "table eight","table nine","table ten", "table eleven","table twelve","table thirteen","table fourteen","table fifteen"]

    matcher=PhraseMatcher(nlp.vocab)
    patterns=[nlp(locs) for locs in custom_locations]

    matcher.add("CUSTOM LOCATIONS", None, *patterns)

    matches=matcher(doc)

    custom_locs= [doc[start:end].text for _, start, end in matches]

    return custom_locs

print(custom_location_extractor(transcript))