from gtts import gTTS
import os
import time   # time.sleep() in seconds
import numpy as np
import csv
import argparse
import configparser

# plays input string in background as app continues
def play_mp3(text_str):
  fname = text_str.replace(" ","_")+".mp3"
  if not (os.path.exists("./mp3_cache/%s" % fname)):
    vobj = gTTS(text=text_str, lang='en', slow=False)
    vobj.save("./mp3_cache/%s" % fname)
  os.system("mpg123 -q ./mp3_cache/%s &" % fname)
  return

# setup time between each exercise
def ex_start(ex_name, t_event=5):
  play_mp3(ex_name)
  time.sleep(t_event)
  return

# countdown sequence marking end of exercise
def ex_countdown (t_event=10):
  time.sleep(t_event-3)
  for i in range(3,0,-1):
    print(i)
    play_mp3(str(i))
    time.sleep(1)
  return

# declare next exercise
def ex_next (ex_name):
  play_mp3("next exercise")
  time.sleep(2)
  play_mp3(ex_name)
  return

# exercise event
def exercise(t_event=30):
  play_mp3("begin")
  time.sleep(t_event-10)
  return

# split exercise event
def splitexercise(t_event=30):
  play_mp3("begin")
  time.sleep(t_event/2.)

  play_mp3("switch sides")
  time.sleep(5)

  play_mp3("begin")
  time.sleep(t_event/2.-10)
  return

# breaktime event
def breaktime (t_event=20):
  play_mp3("take a %d second break" % (t_event+10))
  time.sleep(t_event)


###################################
########### MAIN SCRIPT ###########
###################################

parser = argparse.ArgumentParser(description="Process exercise configuration.")
#parser.add_argument("-t","--time",type=int, default=6, help="Workout duration in minutes.")
parser.add_argument("-c","--conf",type=str, default="default_abs.conf", help="Configuration file name.")

args = parser.parse_args()

################################
# Loading configuration and exercises
################################

config = configparser.ConfigParser()
config.read("./conf/%s" % args.conf)

tTotal  = float(config["Time"]["Total"])
tReady  = int(config["Time"]["Ready"])
tRep    = int(config["Time"]["Rep"])
tBreak  = int(config["Time"]["Break"])

eMode   = config["Exercise"]["Mode"]
eRpS    = int(config["Exercise"]["RpS"])
eCSV    = config["Exercise"]["CSV"]

arrExer = np.genfromtxt("../resources/%s" % eCSV, dtype=str, delimiter=',')
nTotal = np.shape(arrExer)[0]
print("Total possible exercises: %d" % nTotal)

np.random.shuffle(arrExer)

nInt = int(tTotal*2)
nReps = int(tTotal*2 - (tTotal*2)//(eRpS+1))
print("Total session exercises: %d" % nReps)


################################
# Starting sequence
################################

print("App is starting.")
play_mp3("starting abdominal exercises")
time.sleep(3)

print("Duration: %d mins" % tTotal)
play_mp3("%d minutes" % tTotal)
time.sleep(3)



################################
# Workout sequence
################################

rep = 0
for j in range(nInt):
  # breaktime
  if ((j%6)==eRpS):
    play_mp3("break time")
    breaktime(tBreak)

    if ((j+1)!=nReps):
      print("Next exercise: %s" % arrExer[rep+1][0])
      ex_next(arrExer[rep+1][0])

    ex_countdown()
  # exercise
  else:
    print("Current exercise: %s" % arrExer[rep][0])
    ex_start(arrExer[rep][0],tReady)
    if (int(arrExer[rep][1])):
      splitexercise(tRep)
    else:
      exercise(tRep)

    if ((rep+1)==nReps):
      print("almost done!")
      play_mp3("almost done")
    if (((j%6)+1)==5):
      print("Next exercise: break time")
      ex_next("break time")
    else:
      print("Next exercise: %s" % arrExer[rep+1][0]) 
      ex_next(arrExer[rep+1][0])

    ex_countdown(10)

    rep += 1

print("Exercise complete.")
play_mp3("congratulations abdominal exercises completed")
