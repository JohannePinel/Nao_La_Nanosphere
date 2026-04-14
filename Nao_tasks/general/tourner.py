# -*- coding: utf-8 -*- 
import sys
angle = 3.1415
try:
    from naoqi import ALProxy
except ImportError:
    print("Problème avec l'importation de naoqi.")

print(sys.argv[2])
# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 2:
    ROBOT_IP = sys.argv[1]
    rotation = float(sys.argv[2])*angle/180  # Convertir en entier
else:
    print("probleme arguments")


tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559)


id = motion.post.moveTo(0, 0, rotation) 
motion.wait(id, 0)
