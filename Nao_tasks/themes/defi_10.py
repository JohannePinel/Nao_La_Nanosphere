# -*- coding: utf-8 -*- 
import sys
import time
try:
    from naoqi import ALProxy
except ImportError:
    print("Problème avec l'importation de naoqi.")



# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 1:
    ROBOT_IP = sys.argv[1]
    print(ROBOT_IP)
else:
    print("probleme arguments")
speech_recognition = ALProxy("ALSpeechRecognition", ROBOT_IP, 9559)
speech_recognition.pause(True)
tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559) 

turn_angle =  3.14149 # 180 degrees in radians 
tts.say('Bonjour Rachel')

while True : 
    front_head_touch = tactile_touch.getStatus()
    if front_head_touch[7][1] == True:
        tts.say("Tu l'as fait !")
        time.sleep(0.5)
        tts.say("Tu as réussi !")
        time.sleep(0.5)
        tts.say("Je suis très fiere de toi.")
        time.sleep(1)
        tts.say("Tu as donné le meilleur de toi-même,")
        time.sleep(0.5)
        tts.say("et ta determination ainsi que ton sens de l'effort ont payé!")
        time.sleep(1)
        tts.say("Continue de croire en toi et à travailler dur")
        time.sleep(0.5)
        tts.say("car tu es capable de grandes choses !")
        time.sleep(1)
        tts.say("Bravo")
