from gtts import gTTS
import os
import time   # time.sleep() in seconds
import numpy as np
import argparse

# plays input string in background as app continues
def play_mp3(text_str):
  fname = text_str.replace(" ","_")+".mp3"
  if not (os.path.exists("./mp3_cache/%s" % fname)):
    vobj = gTTS(text=text_str, lang='en', slow=False)
    vobj.save("./mp3_cache/%s" % fname)
  os.system("mpg321 -q ./mp3_cache/%s &" % fname)
  return

# setup time between each exercise
def ex_start(ex_name):
  play_mp3(ex_name)
  time.sleep(5)
  play_mp3("begin")
  return

# countdown sequence marking end of exercise
def ex_countdown (t_event):
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
def exercise(t_event=20):
  time.sleep(t_event)
  return

# breaktime event
def breaktime (t_event=20):
  play_mp3("take a 30 second break")
  time.sleep(t_event)


###################################
########### MAIN SCRIPT ###########
###################################

parser = argparse.ArgumentParser(description="Process exercise configuration.")
parser.add_argument('--mode',type=int, default=0, help="Workout mode: 0 - easy; 1 - hard.")
parser.add_argument('--time',type=int, default=6, help="Workout duration in minutes.")

args = parser.parse_args()

# Starting sequence
print("App is starting.")
play_mp3("starting abdominal exercises")
time.sleep(3)

print("Duration: %d mins" % args.time)
play_mp3("%d minutes" % args.time)
time.sleep(2)

if (args.mode==0):
  print("Difficulty: easy")
  play_mp3("easy mode")
elif (args.mode==1):
  print("Difficulty: hard")
  play_mp3("hard mode")
time.sleep(2)


# Loads exercises
exercises = np.genfromtxt('../resources/abs_exercises.csv', dtype=str, delimiter=',')
N_tot = np.shape(exercises)[0]
print("Total possible exercises: %d" % N_tot)

np.random.shuffle(exercises)

N_ex = args.time*2
print("Total session exercises: %d" % N_ex)

# Workout sequence
for j in range(N_ex):
  if ((j%6)==5):    # breaktime
    play_mp3("break time")
    breaktime()

    if ((j+1)!=N_ex):
      print("Next exercise: %s" % exercises[j+1])
      ex_next(exercises[j])

    ex_countdown(10)
  else              # exercise:
    print("Current exercise: %s" % exercises[j])
    ex_start(exercises[j])
    exercise()

    if ((j+1)==N_ex):
      print("almost done!")
    if (((j%6)+1)==5):
      print("Next exercise: break time")
      ex_next("break time")
    else:
      print("Next exercise: %s" % exercises[j+1]) 
      ex_next(exercises[j])

    ex_countdown(10)

print("Exercise complete.")
play_mp3("congratulations abdominal exercises completed")
