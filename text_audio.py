from gtts import gTTS
import os

file = open("text.txt", "r").read().replace("\n", " ")

language = 'en'

speech = gTTS(text = str(file), lang = language, slow = False)

audio_filename = input("Set filename for audio: ")

speech.save(audio_filename+".mp3")

#os.system("start ") # enter filename after the start