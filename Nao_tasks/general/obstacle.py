# -*- coding: utf-8 -*- 
import sys
try:
    from naoqi import ALProxy
except ImportError:
    print("Problème avec l'importation de naoqi.")



# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 1:
    ROBOT_IP = sys.argv[1]
   
else:
    print("probleme arguments")

print(ROBOT_IP)

print("ok")

tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559)


tts.say("Je n'ai pas encore été programmé pour cette missions")
