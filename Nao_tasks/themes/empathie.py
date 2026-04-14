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



time.sleep(2.2857142857142856)

time.sleep(3.2857142857142856)

tts.say("Salut l’équipe") 
time.sleep(0.5) 
tts.say("Ça va super bien aujourd'hui, merci") 
time.sleep(0.5) 
tts.say("Et toi, comment te sens-tu") 
time.sleep(0.5) 

time.sleep(12.428571428571429)

tts.say("Oh, ne t'inquiète pas, on va trouver comment les aider") 
time.sleep(0.5) 

time.sleep(6.785714285714286)

tts.say("Bien sûr") 
time.sleep(0.5) 
tts.say("Imaginez que l’empathie est un pouvoir magique qui te permet de comprendre les émotions de tes amis") 
time.sleep(0.5) 

time.sleep(8.285714285714286)

tts.say("Quand quelqu'un est en colère, tu peux l'écouter vraiment et lui dire des mots gentils comme Je comprends pourquoi tu es en colère") 
time.sleep(0.5) 
tts.say("Ou bien, tu peux le consoler en lui offrant un sourire ou en lui proposant de jouer ensemble pour lui changer les idées") 
time.sleep(0.5) 

time.sleep(4.428571428571429)

tts.say("Bien sûr que oui") 
time.sleep(0.5) 
tts.say("Être empathique permet à tout le monde d'être plus heureux") 
time.sleep(0.5) 
tts.say("Quand tu montres à tes amis que tu te soucies d'eux et que tu veux les aider, ça rend vos amitiés encore plus fortes et joyeuses") 
time.sleep(0.5) 

time.sleep(9.357142857142858)

tts.say("Oui") 
time.sleep(0.5) 
tts.say("Si un ami est joyeux, tu peux partager cette émotion avec lui en célébrant ensemble et en partageant des moments rigolos") 
time.sleep(0.5) 

time.sleep(9.071428571428571)

tts.say("Les adultes peuvent montrer l'exemple en étant empathiques nous-mêmes, en écoutant attentivement leurs sentiments et en les encourageant à parler de leurs émotions") 
time.sleep(0.5) 
tts.say("Ça leur montre que c'est normal d'être gentil et de se soucier des autres") 
time.sleep(0.5) 

time.sleep(13.285714285714286)

time.sleep(3.5)

tts.say("Oh oui, j'aimerais beaucoup être dans votre équipe") 
time.sleep(0.5) 
tts.say("C'est super de discuter de ça avec vous") 
time.sleep(0.5) 
tts.say("Ensemble, nous pouvons créer une équipe où chacun se sent écouté, compris et aimé") 
time.sleep(0.5) 

time.sleep(2.7857142857142856)

tts.say("À bientôt, les amis") 
time.sleep(0.5) 

