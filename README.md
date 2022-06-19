ASCII_ART_GENERATOR
Converting a given image and video into Ascii form of it.

HOW TO RUN THE PROJECT

 Some libraries are required to be installed for this project to run:
 
     PIL(Pillow)
     Open_CV
     Numpy
     
WORKING OF THE PROJECT

 The following code is taking the sample video as input and converting it into frames and saving it into a folder named as "images" which will be craeted using os.mkdir("images")
 and count is the number of frames in the video.

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
Now we have different images in the folder, it's time to convert them into ascii art 
  Loop through the folder to get images one by one
  For every image we will get height and width of it and resize it accordingly,now using nested loop we can loop through every pixel of the image and taking avg of     (r,g,b) value of it to map the characters present in "chars" acording to the intensity of every pixel.The character array is arranged in a way decreasing white space occupied by each character.Then save the output image in a folder.
  
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
Now we have ascii image of each frame and the last step is to combine the frames to convert it into a video
Check for the video properties that is what was the frame rate when the video was captured,and looping through the ascii folder we are combining them using the following code

          fourcc=cv2.VideoWriter_fourcc(*'mpv4')
          video=cv2.VideoWriter("asciiVideo.mp4",fourcc,15,(iw,ih))
          for i in range(count):
              image="ascii/ascimg"+str(i)+".jpg"
              video.write(cv2.imread(image))
          cv2.destroyAllWindows()
          video.release()

          
LEARNINGS FROM THE PROJECT

      Got a good introduction of Open_Cv and PIL libraries.
      Learnt to create new folders and looping through them.
      And final and most important-The mapping of characters according to the intensity of the pixel of image.


REFERENCES
      https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
      https://www.geeksforgeeks.org/python-pil-imagedraw-draw-text/
      https://moonbooks.org/Articles/How-to-add-text-on-an-image-using-pillow-in-python-/
