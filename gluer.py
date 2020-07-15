import cv2
import os

image_folder = r"C:\Users\##########\Videos\cocomelon\\"
video_name = r"C:\Users\##########\Videos\out1.mkv"

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 30, (width,height))

count = 0;

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))
    print(count)
    count+=1

cv2.destroyAllWindows()
video.release()