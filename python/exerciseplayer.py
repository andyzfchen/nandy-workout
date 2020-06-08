from gtts import gTTS
import os
import time   # time.sleep() in seconds
import numpy as np
import csv
import argparse
import configparser

class ExercisePlayer(object):
  """ Player object that stores and outputs exercise sequences. """

  def __init__(self, fConf):
    self.config = configparser.ConfigParser()
    self.config.read("./conf/%s" % fConf)

    self.tTotal       = float(self.config["Time"]["Total"])
    self.tReady       = int(self.config["Time"]["Ready"])
    self.tRep         = int(self.config["Time"]["Rep"])
    self.tRepTimes    = list(map(int,(self.config["Time"]["RepTimes"]).split(":")))
    self.tBreak       = int(self.config["Time"]["Break"])

    self.eMode        = self.config["Exercise"]["Mode"]
    #self.eRpS         = int(self.config["Exercise"]["RpS"])
    self.eRpS         = len(self.tRepTimes)
    self.eDifficulty  = list(map(int,(self.config["Exercise"]["Difficulty"]).split(":")))
    self.eCSV         = self.config["Exercise"]["CSV"]

    temp              = np.genfromtxt("../resources/%s" % self.eCSV, dtype=str, delimiter=',')
    self.arrExer      = [[x for x in temp if int(x[2])==0],[x for x in temp if int(x[2])==1]]

    self.nTotal   = np.shape(self.arrExer)
    self.nInt     = int(self.tTotal*2)
    self.nRep     = int(self.tTotal*2 - (self.tTotal*2)//(self.eRpS+1))

    print("Total possible exercises: %d" % self.nTotal)

    print("Total session exercises: %d" % self.nRep)

  def randomizeExercise(self):
    """ randomizes the exercise name array """
    for i in range(len(self.arrExer)):
      np.random.shuffle(self.arrExer[i])

  def play_mp3(self, text_str, exact=False):
    """ play mp3 file """
    fName = text_str.replace(" ","_")

    if exact:
      if not os.path.exists(os.path.join(".","mp3_cache",fName+".mp3")):
        self.gen_gtts(text_str)

      fPlay = os.path.join(".","mp3_cache",fName+".mp3")
    else:
      files = [x[:-1] for x in os.popen("ls ./mp3_cache/%s*" % fName)]
      fPlay = ''

      if len(files):
        fPlay = files[int(np.floor(np.random.random()*len(files)))]
      else:
        self.gen_gtts(text_str)
        fPlay = os.path.join(".","mp3_cache",fName+".mp3")


    os.system("mpg123 -q %s &" % fPlay)
    return

  def gen_gtts(self, text_str):
    """ generate gtts mp3 file """
    fName = text_str.replace(" ","_")+'.mp3'
    print("Generating mp3: %s" % fName)
    vobj = gTTS(text=text_str, lang='en', slow=False)
    vobj.save("./mp3_cache/%s" % fName)

  def gen_all_exercise_mp3(self):
    """ generate all exercise mp3 files """
    names = [x[0] for sublist in self.arrExer for x in sublist]
    for x in names:
      fName = x.replace(" ","_")+".mp3"
      if not os.path.exists(os.path.join(".","mp3_cache",fName)):
        self.gen_gtts(x)

  def ex_start(self, ex_name, t_event=5):
    """ setup time between each exercise """
    self.play_mp3(ex_name)
    time.sleep(t_event)
    return

  def ex_countdown(self, t_event=8):
    """ countdown sequence marking end of exercise """
    time.sleep(t_event-3)
    for i in ["three","two","one"]:
      print(i)
      self.play_mp3(i,exact=True)
      time.sleep(1)
    return

  def ex_next(self, ex_name):
    """ declare next exercise """
    self.play_mp3("next exercise")
    time.sleep(2)
    self.play_mp3(ex_name)
    return

  def exercise(self, t_event=30):
    """ exercise event """
    print("Begin")
    self.play_mp3("begin")
    time.sleep(t_event-10)
    return

  def splitexercise(self, t_event=30):
    """ split exercise event """
    print("Begin")
    self.play_mp3("begin")
    time.sleep(t_event/2.)

    self.play_mp3("switch sides")
    time.sleep(5)

    self.play_mp3("begin")
    time.sleep(t_event/2.-10)
    return

  def breaktime(self, t_event=20):
    """ breaktime event """
    self.play_mp3("take a %d second break" % (t_event))
    time.sleep(t_event-10)



