import cv2
import os
from os.path import isdir, isfile, join

input_path = './tmp/Camera1/'
output_video = 'video.mp4'
fps = 15
frames = []

directories = [directory for directory in os.listdir(input_path) if isdir(join(input_path, directory))]
directories.sort()

for di in range(len(directories)):
  path = input_path + directories[di]
  files = [file for file in os.listdir(path) if isfile(join(path, file))]
  files.sort()

  for fi in range(len(files)):
    filename = path + '/' + files[fi]
    img = cv2.imread(filename)

    # Remove black frames
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if int(cv2.countNonZero(img_gray)) < 2070000:
     continue

    frames.append(img)

out = cv2.VideoWriter(output_video,cv2.VideoWriter_fourcc(*'H264'), fps, (1920, 1080))
for i in range(len(frames)):
    out.write(frames[i])
out.release()
