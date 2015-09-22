import sys
import time
import random

import motion
from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech","nao.local",9559)
x= tts.setLanguage('chinese')
tts.say('Hello world ! How are you today ?')
print x