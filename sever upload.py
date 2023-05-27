import cv2 as cv
from datetime import datetime
import ftplib

session = ftplib.FTP()
session.connect('172.30.1.78',21 )
session.login("invisible","qwert11")
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('open failed')
    exit()

while True:
    ret,img = cap.read()
    if not ret:
        print("Can't read camera")
        break


    now = datetime.now()
    cv.imshow("PC_camera",img)

    img_fileName = now.strftime("%Y-%m-%d%H%M%S")+'.png'
    img_captured = cv.imwrite(img_fileName,img)

    uploadfile = open(img_fileName,mode = 'rb')

    session.encoding = 'utf-8'
    session.storbinary('STOR '+img_fileName,uploadfile)

    uploadfile.close()

    print('send')

    if cv.waitKey(1) == ord('q'):
        break

session.close()
cap.release()
cv.destroyAllWindows()