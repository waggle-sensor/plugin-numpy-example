from main import process_frame
import cv2

cap = cv2.VideoCapture(0)

while True:
    ok, image = cap.read()
    if not ok:
        break
    cv2.imshow("capture", image)
    cv2.waitKey(1)
    print(process_frame(image))

cap.release()
