import cv2


def detect_faces(image_path):

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Detected Faces', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'image.jpg'
detect_faces(image_path)
