from cv2 import cv2

trainedAi = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
trainedEyeAi = cv2.CascadeClassifier('haarcascade_eye.xml')
trainedSmileAi = cv2.CascadeClassifier('haarcascade_smile.xml')


cap = cv2.VideoCapture(0)

while True:
    success_frame_read, frame = cap.read()
    grayscaledFr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faceCoordinates = trainedAi.detectMultiScale(grayscaledFr)
    eyeCoordinates = trainedEyeAi.detectMultiScale(grayscaledFr)
    smileCoordinates = trainedSmileAi.detectMultiScale(grayscaledFr)

    for (x, y, w, h) in faceCoordinates:
        cv2.rectangle(frame, (x, y),(x+w, y+h), (255, 0, 0), 10)
        print("hi")

    # for (x, y, w, h) in eyeCoordinates:
    #     cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 10)
    #
    # for (x, y, w, h) in smileCoordinates:
    #     cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 0, 0), 10)


    cv2.imshow("BruhBruhBruhBruh", frame)
    cv2.waitKey(1)

# image
# img = cv2.imread('smile.jpg')
# grayscaledImg = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
#
# faceCoordinates = trainedAi.detectMultiScale(grayscaledImg)
# eyeCoordinates = trainedEyeAi.detectMultiScale(grayscaledImg)
# smileCoordinates = trainedSmileAi.detectMultiScale(grayscaledImg)
#
# for (x, y, w, h) in faceCoordinates:
#     cv2.rectangle(src, (x, y),(x+w, y+h), (255, 0, 0), 10)
#
# for (x, y, w, h) in eyeCoordinates:
#     cv2.rectangle(src, (x, y),(x+w, y+h), (0, 255, 0), 10)
#
# for (x, y, w, h) in smileCoordinates:
#     cv2.rectangle(src, (x, y),(x+w, y+h), (0, 0, 0), 10)
#
# print(eyeCoordinates)
#
# cv2.imshow("BruhBruhBruhBruh", src)
# cv2.waitKey(0)
