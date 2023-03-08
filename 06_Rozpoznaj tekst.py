import speech_recognition as sr
from os import path
from pathlib import Path

from pydub import AudioSegment

# convert mp3 file to wav                                                       
# sound = AudioSegment.from_mp3('{}{}'.format(Path(__file__).parent,'''/podcast.mp3'''))[0:50000]
# sound.export('{}{}'.format(Path(__file__).parent,'''/podcast.wav'''), format="wav")


# transcribe audio file                                                         
AUDIO_FILE = '{}{}'.format(Path(__file__).parent,'''/podcast.wav''')

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file     
        print(str(audio))             

        print("Transcription: " + r.recognize_google(audio))