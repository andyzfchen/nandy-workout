from gtts import gTTS
import os
import time   # time.sleep() in seconds
import numpy as np
import csv
import argparse
import configparser
import exerciseplayer as ep

parser = argparse.ArgumentParser(description="Process exercise configuration.")
parser.add_argument("-c","--conf",type=str, default="default_abdominal.conf", help="Configuration file name.")
args = parser.parse_args()

player = ep.ExercisePlayer(args.conf)

print("App is starting.")
player.play_mp3("starting %s exercises" % player.eMode)
time.sleep(3)

print("Duration: %.1f mins" % player.tTotal)
player.play_mp3("%.1f minutes" % player.tTotal)
time.sleep(3)

player.gen_all_exercise_mp3()

player.randomizeExercise()

for j in range(player.nInt):
  diff = player.eDifficulty[j%player.eIpS]
  iexer = player.counter[diff]%player.nDiff[diff]
  player.counter[diff] += 1
  nextdiff = player.eDifficulty[(j+1)%player.eIpS]
  inextexer = player.counter[nextdiff]%player.nDiff[nextdiff]
  player.counter[diff] -= 1
  print("current diff: %d" % diff)
  print("current index: %d" % iexer)
  print("next diff: %d" % nextdiff)
  print("next index: %d" % inextexer)

  # breaktime
  if ((j%(player.eRpS+1))==player.eRpS):
    # normal break
    print("break time")
    player.breaktime(player.tBreak)

    # not last interval
    if ((j+1)!=player.nInt):
      print("Next exercise: %s" % player.arrExer[nextdiff][inextexer][0])
      player.ex_next(player.arrExer[nextdiff][inextexer][0])

    player.ex_countdown()

  # exercise
  else:
    print("Current exercise: %s" % player.arrExer[diff][iexer][0])
    player.ex_start(player.arrExer[diff][iexer][0],player.tReady)

    # split exercise
    if (int(player.arrExer[diff][iexer][1])):
      player.splitexercise(player.tRepTimes[j%player.eIpS])
    # normal exercise
    else:
      player.exercise(player.tRepTimes[j%player.eIpS])

    # last interval
    if ((j+1)==player.nInt):
      print("almost done!")
      player.play_mp3("almost done")
    # next is break
    elif (((j+1)%(player.eRpS+1))==player.eRpS):
      print("Next exercise: break time")
      player.ex_next("break time")
    # next is exercise
    else:
      print("Next exercise: %s" % player.arrExer[nextdiff][inextexer][0]) 
      player.ex_next(player.arrExer[nextdiff][inextexer][0])

    player.ex_countdown()

  player.next(diff) += 1

print("Exercise complete.")
player.play_mp3("congratulations %s exercises completed" % player.eMode)

