import sys
import os
import platform
 
target_folder = "nao_softwarev1"
current_path = os.getcwd()

def detecter_systeme():
    systeme = platform.system()
    if systeme == "Windows":
        return "\\"
    elif systeme == "Linux":
        return "/"
def naoqi_path_detection(current_path):
    systeme = platform.system()
    if systeme == "Windows":
        naoqi_path = current_path + "\\lib\\windows\\Python27\\Lib\\site-packages\\pynaoqi\\lib"
    elif systeme == "Linux":
        naoqi_path = current_path+ "/lib/linux/&pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327/lib"
    return naoqi_path
       
current_path = os.getcwd()
target_folder = "nao_softwarev2"
while os.path.basename(current_path) != target_folder:
    current_path = os.path.dirname(current_path)
sys.path.append(naoqi_path_detection(current_path))

from naoqi import ALProxy
import time
import os

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


id = motion.post.moveTo(1.5, 0, 0) 
motion.wait(id, 0)


