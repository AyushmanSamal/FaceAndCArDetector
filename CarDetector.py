from cv2 import cv2

#videoCar
cap = cv2.VideoCapture('VOITURE_30f.mov')

while True:
    success, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    carTracker = cv2.CascadeClassifier('car_detector.xml')
    carCoordinates = carTracker.detectMultiScale(gray)
    for (x, y, w, h) in carCoordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 10)
        print("warning")
    cv2.imshow("Live", frame)
    cv2.waitKey(1)







#imageCar

#imgFile = 'Car.png'

# classifierFile = 'car_detector.xml'
#
# img = cv2.imread('Car-dataset-taken-by-Brad-Philip-and-Paul-Updike-California-Institute-of-Technology-It.png')
#
# BnW = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# carTracker = cv2.CascadeClassifier(classifierFile)
#
# carCoordinates = carTracker.detectMultiScale(BnW)
#
# for (x, y, w, h) in carCoordinates:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 10)
#
# cv2.imshow("BruhCar", img)
# cv2.waitKey(0)