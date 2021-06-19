import cv2
import dropbox
import time
import random

startTime=time.time()
def takeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name='img'+ str(number) + '.png'
        cv2.imwrite(img_name,frame)
        startTime=time.time
        result=False
    return img_name 
    print('snapshot taken')
    videoCaptureObject.release
    cv2.destroyAllWindows()
def uploadFile(img_name):
    access_token='sl.AzD6VR6u0A43RTboWvjG7wnQU82yY9D1tv3vA8MCsZqGkkumMbuBSMhC_iFN7X6GV42DSjuT6QTvpSJdzz0osmQBW3Ay6D97YamGObDhZ2LfbkHQDnZDPzSwZJ6VSmlfSPxUWx8'
    file=img_name
    file_from=file
    file_to='/newfolder1/' + (img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
def main():
    while(True):
        if((time.time()-startTime)>=5):
            name=takeSnapshot()
            uploadFile(name)
main()