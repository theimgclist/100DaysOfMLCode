**Day 37 - 16th Aug, 2018:** Face Landmarks Detection    

* Couple of days back, I read about face landmarks/fiducial points 
* Facial landmark detection is a key part of face extraction/recognition  
* Using the same Dlib library that was used for face detection, face landmarks can also be detected  
* I used the code from yesterday's face detection and modified it with the help of Dlib's example  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/facelandmarks.jpg"/></p>    

* Dlib's face landmark detection example provides a trained model to detect the face landmarks
* Using the trained model, landmarks can be detected for a given image
* OpenCV is used to plot the landmard points on  the input image

**Some Useful Links :**  
* [100DaysOfMLCode/facelandmarks.py at master · theimgclist/100DaysOfMLCode · GitHub](https://github.com/theimgclist/100DaysOfMLCode/blob/master/src/facelandmarks.py)
*  [dlib/python_examples at master · davisking/dlib · GitHub](https://github.com/davisking/dlib/tree/master/python_examples)
