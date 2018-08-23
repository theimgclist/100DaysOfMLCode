from imutils import face_utils
import dlib
import cv2
import imutils
import numpy as np


def face_remap(shape):
   remapped_image = cv2.convexHull(shape)
   return remapped_image
   
# load the input image, resize it, and convert it to grayscale
image = cv2.imread("image.jpg")
image = imutils.resize(image, width=500)
face = np.zeros_like(image)
# Using the downloaded trained model
SHAPE_PREDICTOR = "shape_predictor_68_face_landmarks\shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(SHAPE_PREDICTOR)
rects = detector(image, 1)

# loop over the face detections
for (i, rect) in enumerate(rects):
   shape = predictor(image, rect)
   shape = face_utils.shape_to_np(shape)
   remapped_shape = np.zeros_like(shape) 
   feature_mask = np.zeros((image.shape[0], image.shape[1])) 
   remapped_shape = face_remap(shape)
   cv2.fillConvexPoly(feature_mask, remapped_shape[0:27], 1)
   feature_mask = feature_mask.astype(np.bool)
   face[feature_mask] = image[feature_mask]
   cv2.imshow("faceextract",face)
   cv2.waitKey(0)
   cv2.imwrite("faceextract.jpg", face)

   