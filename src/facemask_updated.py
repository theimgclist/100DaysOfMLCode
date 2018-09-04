from imutils import face_utils
import imutils
import numpy as np
import collections
import dlib
import cv2
import os
from glob import glob
import shutil

def face_remap(shape):
   remapped_image = cv2.convexHull(shape)
   return remapped_image

image_folder = 'Images/input/'
save_folder = 'Images/output'
nomask_folder = 'Images/nomask'
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

types = ('*.jpg', '*.png')
image_path_list= []
for files in types:
    image_path_list.extend(glob(os.path.join(image_folder, files)))
total_num = len(image_path_list)

for i, image_path in enumerate(image_path_list):
    # read image
    image = cv2.imread(image_path)
	name = image_path.strip().split('/')[-1][6:]
	print(name)
	image = imutils.resize(image, width=500)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	out_face2 = np.zeros((image.shape[0], image.shape[1]))

	out_face = np.zeros_like(image)
	SHAPE_PREDICTOR = "shape_predictor_68_face_landmarks\shape_predictor_68_face_landmarks.dat"
	# initialize dlib's face detector (HOG-based) and then create the facial landmark predictor
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(SHAPE_PREDICTOR)

	# detect faces in the grayscale image
	rects = detector(gray, 1)
	mask_exists = False
	# loop over the face detections
	for (i, rect) in enumerate(rects):
		"""
		Determine the facial landmarks for the face region, then convert the facial landmark (x, y)-coordinates to a NumPy array
		"""
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)
   

		#initialize mask array
		remapped_shape = np.zeros_like(shape) 
   
		feature_mask = np.zeros((image.shape[0], image.shape[1])) 

		# we extract the face
		remapped_shape = face_remap(shape) 
		cv2.fillConvexPoly(feature_mask, remapped_shape[0:27], 1) 
		feature_mask = feature_mask.astype(np.bool) 
		out_face2[feature_mask] = gray[feature_mask]
		#cv2.imshow("mask_inv", out_face2)
		cv2.waitKey(0)
		#print(out_face2)
		out_face2 = out_face2 * 255
		cv2.imwrite(os.path.join(save_folder, name), out_face2)
		mask_exists = True
	if mask_exists == False : 
		shutil.move(image_path, nomask_folder + "/" + name)
		print("Mask is not created for "+name+". Image is moved out!")
