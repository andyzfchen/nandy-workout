from gtts import gTTS
import os
import numpy as np

exercises = np.genfromtxt('abs_exercises.csv', dtype=str, delimiter=',')
print(exercises)
print(np.shape(exercises))

'''
mytext = 'Welcome to geeksforgeeks!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
os.system("mpg321 -q welcome.mp3 &")
print("testing")
'''
