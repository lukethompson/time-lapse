import cv2
import os
from os.path import isdir, isfile, join

pathIn= './tmp/Camera1/'
pathOut = 'video.mp4'
fps = 15
frame_array = []

directories = [directory for directory in os.listdir(pathIn) if isdir(join(pathIn, directory))]
directories.sort()

for di in range(len(directories)):
  path = pathIn + directories[di]
  files = [file for file in os.listdir(path) if isfile(join(path, file))]
  files.sort()

  for fi in range(len(files)):
    filename = path + '/' + files[fi]
    img = cv2.imread(filename)

    # Remove black frames
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if int(cv2.countNonZero(img_gray)) < 2070000:
     continue

    frame_array.append(img)

out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, (1920, 1080))
for i in range(len(frame_array)):
    out.write(frame_array[i])
out.release()
