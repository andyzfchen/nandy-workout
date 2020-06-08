import os

[os.rename(x[:-1],os.path.splitext(x[:-1])[0]+"_bash"+os.path.splitext(x[:-1])[1]) for x in os.popen("ls ./*.mp3")]
