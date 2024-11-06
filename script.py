import cv2
import os
import makeDirec as mdir

videoName = "chiangrak1_back"
directoryName = videoName
frameStep = 40

video = cv2.VideoCapture(f"sources/{videoName}.mp4")

frameCount = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

print(f'have farme: {frameCount}')

for i in range(frameCount):
    check, frame = video.read()
    
    if i % frameStep == 0:
        cv2.imshow("cap", frame)
        
        mdir.makeDirectory(directoryName) # make directory if not have ever 
        cv2.imwrite(f"output/{directoryName}/{videoName}_img{i}.jpg", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

video.release()
cv2.destroyAllWindows()



