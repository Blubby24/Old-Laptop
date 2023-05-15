from gtts import gTTS
import os
import time
  
mytext = 'New Line'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("TalkingFolder/welcome.mp3")
os.system("start TalkingFolder/welcome.mp3")
time.sleep(1)