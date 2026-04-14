# -*- coding: utf-8 -*- 

ROBOT_IP = "172.24.24.150"
port = 9559
from naoqi import ALProxy

print("test")
speech_recognition = ALProxy("ALSpeechRecognition", ROBOT_IP, 9559)
speech_recognition.pause(True)
tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
tts.say("équipe")