import face_recognition
import cv2
import re

import numpy as np
import requests
from os import listdir
from os.path import isfile, join


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


individuals = 'E:\\khk\\volumeF\\soft1\\WinPython\\settings\\.spyder-py3\\facedetection\\individ\\'
onlyfiles = [f for f in listdir(individuals) if isfile(join(individuals, f))]
data = []
stringall = ''
loop = 0
for individual in onlyfiles:
    print(loop)
    loop = loop + 1
    loadiamge = face_recognition.load_image_file(individuals + individual)
    face_encoding = face_recognition.face_encodings(loadiamge)[0]
    file = open("encodings.txt", "a")
    stringall = ''
    for x in face_encoding:
        stringall = stringall + str(x) + ",\n"
    file.write(stringall)
    file.close()
    file = open("encodingnames.txt", "a")
    file.write(individual + ",")
    file.close()
    data.append(face_encoding)
