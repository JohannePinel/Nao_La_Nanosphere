# -*- coding: utf-8 -*- 
import Tkinter as tk
import sys
import os


try:
    from naoqi import ALProxy
except ImportError:
    print("Problème avec l'importation de naoqi.")
    fenetre = tk.Tk()
    fenetre.geometry("400x250")
    fenetre.title("NAO")
    fenetre.mainloop
    
# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 1:
    ROBOT_IP = sys.argv[1]
else:
    print("probleme arguments")

speech_recognition = ALProxy("ALSpeechRecognition", ROBOT_IP, 9559)
speech_recognition.pause(True)
tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559) 
tts.say("Bonjour moi c'est Nao, aujourdhui je teste avec vous la nouvelle application facilitant mon utilisation")
