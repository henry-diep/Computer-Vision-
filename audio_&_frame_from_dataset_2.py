import json
import os
import cv2
import pafy
import moviepy.editor as mp 
from youtube_dl import YoutubeDL

# Open json files
def fun(filename):
    file = open(filename, 'r')
    file = open(filename, 'r')
    data = json.load(file)
    file.close()

    # Download video from the given url
    # Capture and save frame
    def frame(url):
        video = pafy.new(url)
        best  = video.getbest(preftype='mp4')
        cap = cv2.VideoCapture(best.url)
        check, frame = cap.read()
        i = 0
        while cap.isOpened():
            ret, image = cap.read()
            if ret == False:
                break
            cv2.imwrite('frame' + str(i) + '.jpg', image)
            i+=1
        
        cap.release()
        cv2.destroyAllWindows()
    
    # Download video from the given url
    # Extract audio from the video
    def audio(url):
        audio_downloader = YoutubeDL({'format':'bestaudio'})
        audio_downloader.extract_info(url)

    # Passing urls to the functions
    for ID in data:
        frame(data[ID]['url'])
        audio(data[ID]['url'])
        
# Get json files to open them for urls passing
for filename in os.listdir('C:\\Users\\DELL\\Desktop\\Project'):
    if filename.endswith('.json'):
        fun(str(filename))
  

