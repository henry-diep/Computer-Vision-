# Opens the Video file
import cv2
import os

def fun(path):
    cap = cv2.VideoCapture(path)
    i=0
    #print(cap.isOpened())
    #print(path)
    while cap.isOpened():
        ret, image = cap.read()
        if ret == False:
            break
        cv2.imwrite('frame' + str(i) + '.jpg', image)
        i+=1

    cap.release()
    cv2.destroyAllWindows()



for folder in os.listdir('D:\\UCF101\\UCF-101\\'):
    #print(folder)
    for filename in os.listdir('D:\\UCF101\\UCF-101\\' + folder):
        #print(filename)
        if filename.endswith('.avi'):
            fun('D:\\UCF101\\UCF-101\\' + folder + '\\' + filename)
        else:
            print('error')
    


