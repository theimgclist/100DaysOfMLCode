from imutils import face_utils
import dlib
import cv2
import imutils
import numpy as np


# load the input image, resize it, and convert it to grayscale
image = cv2.imread("image.jpg")
image = imutils.resize(image, width=500)
SHAPE_PREDICTOR = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(SHAPE_PREDICTOR)
rects = detector(image, 1)

# loop over the face detections
for (i, rect) in enumerate(rects):
   (x, y, w, h) = face_utils.rect_to_bb(rect)
   cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
   shape = predictor(image, rect)
   shape = face_utils.shape_to_np(shape)
   for (x, y) in shape:
      cv2.circle(image, (x, y), 2, (0, 255, 255), -1)
   cv2.imshow("facedetection",image)
   cv2.waitKey(0)
   cv2.imwrite("facelandmarks.jpg", image)