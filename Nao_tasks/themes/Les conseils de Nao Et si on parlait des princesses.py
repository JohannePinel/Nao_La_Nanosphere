# -*- coding: utf-8 -*- 
# -*- coding: utf-8 -*- 
import sys
import time

import os

path_to_add = "~/Documents/nao/nao_softwarev3/lib/linux/naoqi/pynaoqi-python2.7-2.8.7.4-linux64-20210819_141148/lib/python2.7/site-packages"

path_to_add = os.path.expanduser(path_to_add)

sys.path.append(path_to_add)

# Maintenant vous pouvez importer naoqi
import naoqi
from naoqi import ALProxy



# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 1:
    ROBOT_IP = sys.argv[1]
else:
    print("probleme arguments")
# Créer une instance du proxy pour ALSpeechRecognition
speech_recognition = ALProxy("ALSpeechRecognition", ROBOT_IP, 9559)

# Désactiver la reconnaissance vocale
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





time.sleep(3.7857142857142856)

time.sleep(1.5)

time.sleep(1.5)

tts.say("Hello l’équipe, Vous avez l’air curieux aujourd’hui…") 
time.sleep(0.5) 

time.sleep(3.4285714285714284)

time.sleep(2.5)

tts.say("Mmmh… Beaucoup disent que c’est une fille avec une robe brillante…Une couronne… Et qui attend qu’un prince vienne la sauver") 
time.sleep(0.5) 

time.sleep(4.214285714285714)

tts.say("Mais ça, c’est faux") 
time.sleep(0.5) 
tts.say("Moi, je connais des princesses… vraiment différentes") 
time.sleep(0.5) 

time.sleep(2.0714285714285716)

tts.say("Tu veux un exemple") 
time.sleep(0.5) 
tts.say("Il y avait une princesse qui s’appelait Yennenga") 
time.sleep(0.5) 
tts.say("Elle vivait en Afrique") 
time.sleep(0.5) 
tts.say("Elle montait à cheval") 
time.sleep(0.5) 
tts.say("Et elle portait une armure") 
time.sleep(0.5) 

time.sleep(3.0)

tts.say("Oui") 
time.sleep(0.5) 
tts.say("Elle était très forte") 
time.sleep(0.5) 
tts.say("Elle protégeait son peuple") 
time.sleep(0.5) 
tts.say("Et elle ne voulait pas attendre qu’on lui dise quoi faire") 
time.sleep(0.5) 

time.sleep(3.5)

tts.say("Je suis sûr qu’elle avait les cheveux en bataille après la bataille") 
time.sleep(0.5) 
tts.say("Et tu sais quoi") 
time.sleep(0.5) 
tts.say("Je crois même qu’il y a des princesses qui courent pieds nus, mangent du chocolat, et qui se mettent de la boue partout") 
time.sleep(0.5) 

time.sleep(1.5)

tts.say("Et certaines princesses… ben… elles pètent") 
time.sleep(0.5) 
tts.say("Et elles mangent leur crotte de nez") 
time.sleep(0.5) 

time.sleep(1.5)

tts.say("Mais c’est vrai") 
time.sleep(0.5) 
tts.say("Les princesses sont des vraies personnes") 
time.sleep(0.5) 
tts.say("Elles ne sont pas parfaites") 
time.sleep(0.5) 
tts.say("Elles ont un cœur, des idées, des bêtises aussi") 
time.sleep(0.5) 
tts.say("Et elles ont le droit d’être comme elles sont") 
time.sleep(0.5) 

time.sleep(5.714285714285714)

tts.say("Non") 
time.sleep(0.5) 
tts.say("Une princesse, ça peut être forte, drôle, têtue, bruyante, timide…Grande ou petite, avec ou sans robe") 
time.sleep(0.5) 

time.sleep(2.357142857142857)

tts.say("Pas du tout") 
time.sleep(0.5) 
tts.say("Certaines ne veulent pas") 
time.sleep(0.5) 
tts.say("Elles préfèrent voyager, construire, inventer, rêver") 
time.sleep(0.5) 

time.sleep(2.0)

tts.say("Alors, qui veut créer sa propre princesse pas comme les autres") 
time.sleep(0.5) 
tts.say("Une princesse avec une cape") 
time.sleep(0.5) 
tts.say("Une qui fait du vélo") 
time.sleep(0.5) 
tts.say("Une qui parle aux oiseaux") 
time.sleep(0.5) 
tts.say("Une qui fait des blagues très nulles") 
time.sleep(0.5) 

time.sleep(2.5714285714285716)

tts.say("Moi aussi") 
time.sleep(0.5) 
tts.say("Et je suis sûr que les enfants en auront encore plus") 
time.sleep(0.5) 

time.sleep(3.5714285714285716)

tts.say("C’est normal, je lis plein de livres et je suis très curieux") 
time.sleep(0.5) 
tts.say("Je sais tout") 
time.sleep(0.5) 

time.sleep(2.2142857142857144)

time.sleep(1.5)
tts.say("Ciao l'équipe") 

time.sleep(1.5)


