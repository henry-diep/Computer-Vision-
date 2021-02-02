# Python code to convert video to audio
import cv2
import moviepy.editor as mp 
  
# Insert Local Video File Path  
clip = mp.VideoFileClip(r'video_path') 
  
# Insert Local Audio File Path 
clip.audio.write_audiofile(r'audio_file_name')

# Capture frames
# Insert video path
cap = cv2.VideoCapture('video_path')
i=0
while(cap.isOpened()):
    ret, image = cap.read()
    if ret == False:
        break
    cv2.imwrite('frame' + str(i) + '.jpg', image)
    i+=1

cap.release()
cv2.destroyAllWindows()
