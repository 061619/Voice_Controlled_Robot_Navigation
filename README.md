# <b>Voice Controlled Robot Navigation</b>
<b>Overview</b>
<br><br>
This project is designed to process spoken commands in real-time, transcribe them into text, and extract meaningful location-based information using Natural Language Processing (NLP). It is particularly useful in applications such as robotic navigation, voice-controlled assistants, and automated ordering systems.
<br><br>
The system follows a structured workflow where it:
<br><br>
Captures spoken commands using a microphone.
Transcribes the speech into text using an Automatic Speech Recognition (ASR) API.
Analyzes the transcribed text using NLP techniques to extract specific location-based entities.
This implementation eliminates the need to manually save and process audio files, making it efficient and seamless. The combination of speech recognition and NLP ensures that users can interact with the system naturally, without requiring manual input.
<br><br>
<b>Technologies Used:</b>
<br>
1. Speech Recognition
<br>
Library: speech_recognition<br>
Captures voice input using a microphone.<br>
Adjusts for ambient noise dynamically to enhance recognition accuracy.<br>
Listens until the user stops recording.<br><br>
2. Automatic Speech Recognition (ASR) API<br>
Spring Lab ASR API (https://asr.iitm.ac.in/internal/asr/decode)<br>
Converts recorded speech into text.<br>
Supports multiple languages (configured for English in this project).<br>
Returns a structured JSON response containing the transcribed text.<br><br>
3. Natural Language Processing (NLP)<br>
Library: spaCy<br>
Processes the transcribed text for further analysis.<br>
Identifies and extracts location-based keywords using the PhraseMatcher module.<br><br>
4. API Communication<br>
Library: requests<br>
Sends the recorded audio data directly to the ASR API.<br>
Receives and processes the JSON response from the API.<br><br>
<b>Project Workflow</b><br><br>
1)Capturing Speech Input<br>
When the user types "listen", the system initializes the microphone and begins recording. Before capturing the speech, the program adjusts for ambient noise to filter out background noise and improve recognition accuracy. This is done using:
<br><br>
recognizer.adjust_for_ambient_noise(source, duration=1)
recognizer.energy_threshold = 300 (Dynamic thresholding for noise filtering)
Once the system is ready, it listens to the user’s speech until the user manually types "stop". This approach ensures that only one command is processed at a time, preventing overlapping speech data.
<br><br>
2) Sending Audio to the Speech Recognition API<br>
Instead of saving the recorded audio as a file and processing it later, the system directly sends the captured audio to the Spring Lab ASR API for transcription.
<br><br>
This is achieved using Python’s io.BytesIO() method, which converts the recorded audio into a byte stream. The byte stream is then sent via an HTTP request to the API, which returns the transcribed text in JSON format.
<br><br>
3)Extracting Relevant Locations Using NLP<br>
Once the transcription is received, the system uses spaCy for further analysis. The extracted text is processed using the PhraseMatcher module, which checks for predefined locations such as:
<br><br>
"table one", "table two", "bill counter", "kitchen", "sandwich counter"
These predefined locations help in understanding the navigation path in the spoken command.
If any of these locations are mentioned in the transcribed text, they are extracted and stored in a list.
<br><br>
<b>Key Features</b>
✅ Real-Time Speech Recognition<br>
✅ Hands-Free Operation<br>
✅ API-Based Speech Transcription<br>
✅ NLP-Based Location Extraction<br>
spaCy’s PhraseMatcher is used to detect location-related keywords from the command.
Helps in robotic navigation and command processing.
<b>Conclusion</b><br>
This project successfully integrates speech recognition, API-based transcription, and NLP processing to create an efficient real-time voice command system. The ability to extract location-based information makes it a valuable tool for various applications, including robotics and automation.
<br><br>
Future improvements could include multi-language support, more advanced NLP models, and real-time feedback mechanisms. 






