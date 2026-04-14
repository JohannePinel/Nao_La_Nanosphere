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





time.sleep(2.4285714285714284)

time.sleep(4.571428571428571)

tts.say("Hello l’équipe") 
time.sleep(0.5) 
tts.say("Je suis très content d’être là") 
time.sleep(0.5) 
tts.say("J’ai plein de choses à vous raconter") 
time.sleep(0.5) 

time.sleep(3.2142857142857144)

tts.say("Aujourd’hui, j’ai envie de parler d’un sujet très important… quelque chose qu’on utilise tous les jours, sans trop y penser") 
time.sleep(0.5) 

time.sleep(2.642857142857143)

tts.say("Du plastique") 
time.sleep(0.5) 

time.sleep(1.6428571428571428)

tts.say("Oui") 
time.sleep(0.5) 
tts.say("Le plastique est partout") 
time.sleep(0.5) 
tts.say("dans les jouets, les bouteilles, les sacs, les emballages… C’est vrai que c’est pratique") 
time.sleep(0.5) 
tts.say("Mais savez-vous qu’il peut faire beaucoup de mal à la nature") 
time.sleep(0.5) 

time.sleep(5.071428571428571)

tts.say("Exactement") 
time.sleep(0.5) 
tts.say("Une fois qu’on n’en a plus besoin, on le jette… mais il ne disparaît pas comme par magie") 
time.sleep(0.5) 
tts.say("Il met parfois plus de 400 ans à se décomposer") 
time.sleep(0.5) 

time.sleep(2.7142857142857144)

tts.say("Tu as tout à fait raison") 
time.sleep(0.5) 
tts.say("Et pendant tout ce temps, il peut se retrouver dans les forêts, les rivières… ou dans les océans") 
time.sleep(0.5) 

time.sleep(3.357142857142857)

tts.say("Les animaux marins, comme les tortues ou les poissons, peuvent croire que le plastique est de la nourriture") 
time.sleep(0.5) 
tts.say("Ils le mangent… et ça les rend très malades") 
time.sleep(0.5) 
tts.say("Parfois, ils n’arrivent même plus à vivre") 
time.sleep(0.5) 

time.sleep(4.428571428571429)

tts.say("Oui") 
time.sleep(0.5) 
tts.say("Il suffit de changer quelques habitudes") 
time.sleep(0.5) 
tts.say("Vous voulez connaître les astuces de Nao, le robot écolo") 
time.sleep(0.5) 

time.sleep(2.5)

tts.say("Toujours jeter les déchets à la poubelle, jamais par terre") 
time.sleep(0.5) 

time.sleep(1.8571428571428572)

tts.say("Utiliser des objets réutilisables comme une gourde ou un sac en tissu") 
time.sleep(0.5) 

time.sleep(1.9285714285714286)

tts.say("Trier ses déchets pour que certains puissent être recyclés") 
time.sleep(0.5) 

time.sleep(1.9285714285714286)

tts.say("Réutiliser un objet au lieu de le jeter tout de suite") 
time.sleep(0.5) 

time.sleep(4.857142857142857)

tts.say("Oui") 
time.sleep(0.5) 
tts.say("Je vais vous décrire un objet, et vous devrez me dire si on le jette dans") 
time.sleep(0.5) 
tts.say("la poubelle normale, la poubelle à cartons, la poubelle à verre ou le compost ") 
time.sleep(0.5) 

tts.say("Dans quelle poubelle on met… une peau de banane") 
time.sleep(0.5) 

time.sleep(1.5)

tts.say("Très bien") 
time.sleep(0.5) 
tts.say("Et maintenant… un papier cadeau") 
time.sleep(0.5) 

time.sleep(2.642857142857143)

tts.say("Dernier objet") 
time.sleep(0.5) 
tts.say("un jouet cassé, tout abîmé") 
time.sleep(0.5) 

time.sleep(4.0)

tts.say("Wouah, bravo") 
time.sleep(0.5) 

tts.say("Vous avez été formidables") 
time.sleep(0.5) 
tts.say("Je suis très fier de vous") 
time.sleep(0.5) 
tts.say("Vous avez compris que chaque geste compte pour protéger notre planète") 
time.sleep(0.5) 

time.sleep(5.571428571428571)

tts.say("On peut lui dire gentiment") 
time.sleep(0.5) 
tts.say("« Tu peux le mettre à la poubelle") 
time.sleep(0.5) 
tts.say("C’est important pour la nature") 
time.sleep(0.5) 
tts.say("» Et si c’est difficile, on en parle à un adulte") 
time.sleep(0.5) 
tts.say("L’important, c’est de montrer l’exemple") 
time.sleep(0.5) 

time.sleep(6.714285714285714)

tts.say("Très bonne idée") 
time.sleep(0.5) 
tts.say("C’est ce qu’on appelle le recyclage créatif") 
time.sleep(0.5) 
tts.say("On peut transformer une vieille bouteille en arrosoir, un pot de yaourt en boîte à crayons… L’imagination, c’est une super alliée de la planète") 
time.sleep(0.5) 

time.sleep(5.142857142857143)

tts.say("Je suis toujours là pour vous aider à grandir et à réfléchir") 
time.sleep(0.5) 
tts.say("On peut être petits et faire de grandes choses") 
time.sleep(0.5) 

time.sleep(1.5)

time.sleep(1.5)
tts.say("Ciao l'équipe") 


time.sleep(1.5)
