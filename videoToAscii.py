import cv2
import os
from turtle import width
from PIL import Image,ImageDraw,ImageFont

import math

os.mkdir("images")
os.mkdir("ascii")

# sample video is taken as input
vidObj=cv2.VideoCapture("Samplevideo.mp4")

# Now we will be converting entire video into frames and we will count number of total frames generated
count=0
flag=1
while flag:
    flag,image=vidObj.read()
    try:
        cv2.imwrite("images/frame%d.jpg"%count,image)
    except:
        break
    count+=1

chars="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
# chars="#$@Wo-    "[::-1]
charArray=list(chars)
charLength=len(charArray)
intervalLength=charLength/256
scaleFactor=0.3
oneCharWidth=8
oneCharHeight=18
fnt=ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf',15)
def getChar(inputInt):
    return charArray[math.floor(inputInt*intervalLength)]

# We will be iterating through the folder of images(frames) to convert each image into Ascii Image and save each image with diff name in diff folder
for l in range(count):
    im=Image.open("images/frame"+str(l)+".jpg")
    width,height=im.size
    im=im.resize((int(scaleFactor*width),int(scaleFactor*height*(oneCharWidth/oneCharHeight))),Image.NEAREST)
    pix=im.load()
    width,height=im.size
    # print(width,height)

    outputImage=Image.new('RGB',(oneCharWidth*width,oneCharHeight*height),color=(20,20,24))
    d=ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            r,g,b=pix[j,i]
            h=int((r+g+b)/3)
            pix[j,i]=(h,h,h)
            d.text((j*oneCharWidth,i*oneCharHeight),getChar(h),font=fnt,fill=(r,g,b))

    outputImage.save("ascii/ascimg"+str(l)+".jpg")

frame=cv2.imread("ascii/ascimg0.jpg")

# Iterate through the ascii image folder to combine them into a single video
ih,iw,il=frame.shape
fourcc=cv2.VideoWriter_fourcc(*'mpv4')
video=cv2.VideoWriter("asciiVideo.mp4",fourcc,15,(iw,ih))
for i in range(count):
    image="ascii/ascimg"+str(i)+".jpg"
    video.write(cv2.imread(image))
cv2.destroyAllWindows()

#  WAIT FOR SOMETIME TO GET FRAMES CONVERTED INTO A VIDEO   

video.release()

