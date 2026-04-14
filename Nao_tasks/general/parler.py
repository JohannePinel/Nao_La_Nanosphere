# -*- coding: utf-8 -*- 
import sys
import Tkinter as Tk

try:
    from naoqi import ALProxy
except ImportError:
    print("Problème avec l'importation de naoqi.")

global texte


sys.path.append("C:\Python27\python.exe")

# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 2:
    ROBOT_IP = sys.argv[1]
    argument = sys.argv[2]  # Convertir en entier
else:
    print("probleme arguments")

speech_recognition = ALProxy("ALSpeechRecognition", ROBOT_IP, 9559)
speech_recognition.pause(True)

tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559)



print("Argument", argument)


if argument == "meteo":
    tts.say("Aujourd'hui a Saint Sulpice il fait 10 degrées, un soleil est attendu dans la journée ")
elif argument == "actualite":
    tts.say("Cette semaine la flamme olympique est arrivé en France, elle traverse les differentes grandes villes de mains en mains de sportifs et célébrites françaises")

elif argument == "programmation":
    tts.say("je suis programmé grâce à Gabriel qui me donne les instructions en python pour que je puisse les éxecuter, nous verrons la semaine prochaine comment écrire votre premier code")



