**Day 38 - 17th Aug, 2018:** Face Extraction   

* We know how to detect face and also the 68 landmarks coordinates 
* Using the 68 landmark outline and OpenCV we can extract the these from the given face image  
* Used OpenCV's convexHull() function to remap the landmark coordinates for better outline  
* Used fillConvexPoly() method to draw the extracted face

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/faceextract.jpg"/></p>    

* Dlib's face landmark detection example provides a trained model to detect the face landmarks
* Using the trained model, landmarks can be detected for a given image

**Some Useful Links :**  
* [100DaysOfMLCode/faceextraction.py at master · theimgclist/100DaysOfMLCode · GitHub](https://github.com/theimgclist/100DaysOfMLCode/blob/master/src/faceextraction.py)
* [dlib/python_examples at master · davisking/dlib · GitHub](https://github.com/davisking/dlib/tree/master/python_examples)
