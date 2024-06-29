import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
from datetime import datetime
from datetime import date

def voice_to_text():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # Using google speech recognition
            text = r.recognize_google(audio_text)
            return text
        except:
            return 0
    
    
def text_to_voice(text, language='en'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Save the converted audio to a file
    tts.save("output.mp3")
    
    # Play the converted audio file
    os.system("mpg321 output.mp3")
    
        
def search_words_in_text(text, words):
    for word in words:
        if word in text:
            return word
    return 0

def respond(data):
	#Websites
	if search_words_in_text(data, ["Google","google"]):
		url = "https://www.google.com"
		webbrowser.open(url)
	if search_words_in_text(data, ["favelin"]):
		url = "https://favelin.com/"
		webbrowser.open(url)
	
	#Timing
	if search_words_in_text(data, ["Time","time"]):
		text_to_voice(str(datetime.now().time()))
	if search_words_in_text(data, ["Date","date"]):
		text_to_voice(str(date.today()))
        


# main
text_to_voice("Hello mariouma, How can I help you?")
while 1:
	recognized_text = voice_to_text()
	if recognized_text:
		print(f"You said: {recognized_text}")
		respond(recognized_text)

