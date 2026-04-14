# -*- coding: utf-8 -*- 
import sys
import Tkinter as Tk

try:
    from naoqi import ALProxy
except ImportError:
    print("Problème avec l'importation de naoqi.")


sys.path.append("C:\Python27\python.exe")

# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 2:
    ROBOT_IP = sys.argv[1]
    texte = sys.argv[2]  # Convertir en entier
    print(texte)
else:
    print("probleme arguments")
    
print("le texte est", texte)
if "\xe9" in texte:
    print("ok")
texte = texte.replace("\xe9", "é")

tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559)
tts.say(texte)