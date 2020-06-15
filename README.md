# Nandy Workout App
Abdominal workout applet

## Javacript Mobile App

### To run the Mobile App:
1. First time users:   
install expo-cli with `yarn global add expo-cli`  
Clone the repository and run `npm install`  
2. Run `expo start`. A QR code should appear
3. Download the Expo App on your phone, scan the QR code on "tunnel" connection

### Packages Used:
- React Native Elements
- React Navigation

## Python Script App

Requirements and dependencies:
- python 3.x
- numpy
- gTTS

### Usage
1. Go to the python directory using `cd ./python`.
2. Create an exercise list for the desired exercise routine in the `resources` directory. Use the default csv files as a timeplae and save the file with the `.csv` extension.
3. Create a configuration file for the desired exercise routine in the `conf` directory. Use the default conf files as a template and save the file with the `.conf` extension.
4. Run the script using `python doExercise.py`. Default exercise conf file used is `default_abs.conf`. Choose a different conf file by using `python doExercise.py --conf example.conf`.
