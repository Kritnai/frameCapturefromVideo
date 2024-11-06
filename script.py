import cv2
import os

videoName = "chiangrak1_back"
directoryName = videoName
frameStep = 40


def makeDirectory(nameOfDirectory):
    # Setting exist_ok=True will prevent an error if the directory already exists.
    os.makedirs(f"output/{nameOfDirectory}", exist_ok=True)
    


video = cv2.VideoCapture(f"sources/{videoName}.mp4")

frameCount = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

print(f'have farme: {frameCount}')

for i in range(frameCount):
    check, frame = video.read()
    
    if i % frameStep == 0:
        cv2.imshow("cap", frame)
        
        makeDirectory(directoryName) # make directory if not have ever 
        cv2.imwrite(f"output/{directoryName}/{videoName}_img{i}.jpg", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

video.release()
cv2.destroyAllWindows()

