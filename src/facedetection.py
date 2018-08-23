from imutils import face_utils
import dlib
import cv2
import imutils


# load the input image, resize it, and convert it to grayscale
image = cv2.imread("image.jpg")
image = imutils.resize(image, width=500)
detector = dlib.get_frontal_face_detector()
rects = detector(image, 1)

# loop over the face detections
for (i, rect) in enumerate(rects):
   (x, y, w, h) = face_utils.rect_to_bb(rect)
   cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
   cv2.imshow("facedetection",image)
   cv2.waitKey(0)
   cv2.imwrite("face.jpg", image)

   