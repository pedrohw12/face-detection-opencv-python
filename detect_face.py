import glob
from os import listdir, walk
import cv2
from os.path import isfile, join
import numpy
from imutils import paths
import imutils

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

images = [cv2.imread(file) for file in glob.glob("D:\Desktop\face-detection-improved\data\*.jpg")]

##################################################################################################
mypath= "D:/Desktop/face-detection-improved/data"

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath, f)) ]

images = numpy.empty(len(onlyfiles), dtype=object)

for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread(join(mypath, onlyfiles[n]))

##################################################################################################

def findFaces(photo):
    img = cv2.imread(photo)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

    print("Found {0} faces !".format(len(faces)))

    for (x, y, w, h) in faces:
      cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

      # cv2.imshow('Faces found', img)
      # cv2.waitKey(0)


n = 0

# while n <= len(images):
#   for item in onlyfiles:
#     findFaces(item.join('""'))
#   n += 1

for item in onlyfiles:
  print(item.join('""'))

# findFaces('foto.jpg')







