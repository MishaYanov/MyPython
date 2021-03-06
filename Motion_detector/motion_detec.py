#pip install pandas, cv2

import cv2, time, pandas
from datetime import datetime
first_frame=None



statusList=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])


video=cv2.VideoCapture(0)
while True:
    check, frame=video.read()
    status=0
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (21,21), 0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    threshD=cv2.threshold(delta_frame,30,255, cv2.THRESH_BINARY)[1]
    threshD=cv2.dilate(threshD, None, iterations=2)

    (cnts,_) =cv2.findContours(threshD.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) <1000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,0),3)

    statusList.append(status)
    statusList=statusList[-2:]

    if statusList[-1]==1 and statusList[-2]==0:
        times.append(datetime.now())
    if statusList[-1]==0 and statusList[-2]==1:
        times.append(datetime.now())

    print(status)
    #cv2.imshow("gray frame", gray)
    #cv2.imshow("delta",delta_frame)
    #cv2.imshow("trsh",threshD)
    cv2.imshow("frame",frame)

    key=cv2.waitKey(1)

    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

for i in range(0, len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("times.csv")

video.release()
cv2.destroyAllWindows