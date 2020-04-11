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
  time.sleep(1)
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
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

exercises = np.genfromtxt('../data/abs_exercises.csv', dtype=str, delimiter=',')
print(exercises)
print(np.shape(exercises))


# Starting sequence
print("App is starting.")
print("Duration: $time mins")
print("Hardcore: $hard")

say "Starting abdominal exercises."
say "$time minutes."
if $hard
then
  say "Hard mode."
else
  say "Easy mode."
fi
sleep 2
echo

