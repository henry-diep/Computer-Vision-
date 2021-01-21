# Opens the Video file
import cv2
# Creates new Video
# Replace 0 with path to existing video
cap= cv2.VideoCapture(0)
i=0
while(cap.isOpened()):
    ret, image = cap.read()
    if ret == False:
        break
    cv2.imwrite('frame' + str(i) + '.jpg', image)
    i+=1
 
cap.release()
cv2.destroyAllWindows()
