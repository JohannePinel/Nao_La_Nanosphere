# -*- coding: utf-8 -*- 
# -*- coding: utf-8 -*- 
import sys
import time

import os


# Maintenant vous pouvez importer naoqi
import naoqi
from naoqi import ALProxy



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

turn_angle =  3.14149 # 180 degrees in radians 
tts.say('Bonjour Ève')


while True : 
    front_head_touch = tactile_touch.getStatus()
    if front_head_touch[7][1] == True:
        break





time.sleep(2.4285714285714284)

time.sleep(5.5)

tts.say("Salut l'équipe !") 
time.sleep(0.5) 
tts.say("ça va très bien, merci.") 
time.sleep(0.5) 
time.sleep(0.5) 
tts.say("Et vous ?") 

time.sleep(10)

tts.say("Ah, mission super nez activée !") 
time.sleep(0.5) 

time.sleep(4.19)

tts.say("Bien sûr !") 
time.sleep(0.5) 
tts.say("Dans ton nez il y a un petit sytème magique qui attrape la poussière, les microbes et les saletés quand tu respires.") 
time.sleep(0.5) 
tts.say("Les crottes de nez ce sont les saletés que ton corps a capturées pour te protéger.") 
time.sleep(0.5) 


time.sleep(3)

tts.say("On remet dans sa bouche ce que le corps a justement essayé d'éliminer !") 
time.sleep(0.5) 
tts.say("Les microbes peuvent entrer dans le ventre et parfois rendre malade !") 
time.sleep(0.5) 

time.sleep(4.09)


tts.say("Parfois parce que ça gratte, parfois parce qu’ils s’ennuient, ou simplement parce qu’ils ne savent pas encore que ce n’est pas une bonne idée.") 
time.sleep(0.5) 

time.sleep(2.56)

tts.say("On peut leur apprendre à utiliser un mouchoir quand ça les gêne.") 
time.sleep(0.5) 
tts.say("Et ensuite, très important : se laver les mains.") 
time.sleep(0.5) 
tts.say("Les mains propres, c'est la clé !") 
time.sleep(0.5) 

time.sleep(2)

tts.say("On lui rappelle calmement, sans se moquer") 
time.sleep(0.5) 
tts.say("Apprenbdre, ça prend du temps") 
time.sleep(0.5) 
tts.say("On peut dire : ") 
time.sleep(0.5) 
tts.say("Ton nez travaille pour te protéger, on va l'aider avec un mouchoir.") 
time.sleep(0.5) 

time.sleep(3.09)

tts.say("Exactement !") 
time.sleep(0.5) 
tts.say("On ne gronde pas, on explique.") 
time.sleep(0.5) 
tts.say("Le corps est intelligent, et on apprend à en prendre soin.") 
time.sleep(0.5) 

time.sleep(1.38)

tts.say("À bientôt l'équipe")
time.sleep(0.5)
tts.say("Mission nez propre et mains propres réussie !!")


