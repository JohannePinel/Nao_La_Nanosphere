# -*- coding: utf-8 -*- 
import sys
import os

# Maintenant vous pouvez importer naoqi
import naoqi
from naoqi import ALProxy


# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 2:
    ROBOT_IP = sys.argv[1]
    
else:
    print("probleme arguments")


tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559)


right_arm_joints = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]

# Angles in radians for raising the arm
right_arm_angles = [0,-6, 6.0, 0, 0.0]

# Time to reach the target angles in seconds
time_to_reach = 0.2

# Use ALMotion's setAngles method to set the angles for the right arm
motion.setAngles(right_arm_joints, right_arm_angles, time_to_reach)