from turtle import width
from PIL import Image,ImageDraw,ImageFont

import math

# chars="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
# chars="$@B%8&WM##Goahkbdpqwm$$$$#####zcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
chars="#Wo- "
charArray=list(chars)
charLength=len(charArray)
intervalLength=charLength/256
scaleFactor=0.3
oneCharWidth=8
oneCharHeight=18

def getChar(inputInt):
    return charArray[math.floor(inputInt*intervalLength)]

text_file=open("Output.txt","w")

im=Image.open("test.jpg")

fnt=ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf',15)

# newSize=(1000,1000)
width,height=im.size
im=im.resize((int(scaleFactor*width),int(scaleFactor*height*(oneCharWidth/oneCharHeight))),Image.NEAREST)
pix=im.load()
width,height=im.size
print(width,height)

outputImage=Image.new('RGB',(oneCharWidth*width,oneCharHeight*height),color=(20,20,24))
d=ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r,g,b=pix[j,i]
        h=int((r+g+b)/3)
        pix[j,i]=(h,h,h)
        text_file.write(getChar(h))
        d.text((j*oneCharWidth,i*oneCharHeight),getChar(h),font=fnt,fill=(r,g,b))

    text_file.write('\n')


outputImage.save('output.png')