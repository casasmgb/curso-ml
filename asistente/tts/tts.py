from gtts import gTTS
import os

def simpleTTS(txt, player):
    audio = gTTS(text=txt, lang='es', slow=False)
    audio.save("audio.mp3")
    os.system(f'{player} audio.mp3')
    os.system('rm audio.mp3')



