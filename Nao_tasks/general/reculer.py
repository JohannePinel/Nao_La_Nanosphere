# -*- coding: utf-8 -*- 
import sys
try:
    from naoqi import ALProxy
except ImportError:
    print("Problème avec l'importation de naoqi.")



# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 2:
    ROBOT_IP = sys.argv[1]
    distance = float(sys.argv[2])/100  # Convertir en entier
else:
    print("probleme arguments")

tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559)


id = motion.post.moveTo(-distance, 0, 0) 
motion.wait(id, 0)
