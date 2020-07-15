import cv2
from PIL import Image
from time import sleep
from PIL import ImageFilter
import os



cap = cv2.VideoCapture(r'C:\Users\##########\Videos\pewdiepie-cocomelon-intro.mp4')
count = 0

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # framename= "%05d" % (count * 2)
        framename= "%05d" % (count)

        # this is just an upscale of the pic
        frame = cv2.resize(frame,(1920,1080))
        #this resizes and saves the pic
        imgFolder = r"C:\Users\##########\Videos\cocomelon\\"
        cv2.imwrite(imgFolder + str(framename) + ".jpg".format(count), frame)


        jpegFile = imgFolder + str(framename) + ".jpg"
        pngFile = imgFolder + str(framename) + ".png"

        # print
        # IF YOU WANT THE ACTUAL SOURCE CODE FOR THE JAVA JAR, go to my other ASCII github repo
        os.system("java -jar 1080p.jar " + "\"" + jpegFile + "\" \"" + pngFile + "\"")


        # the writing was in case I wasn't able to filter by png
        with open(imgFolder + "files.txt", "a") as myfile:
            myfile.write(imgFolder + str(framename) + ".png".format(count) + "\n")

        


        count += 1 # i.e. at 30 fps, this advances one second
        cap.set(1, count)
        print(count)
    else:
        cap.release()
        break



