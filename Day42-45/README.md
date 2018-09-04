**Day 42 to 45 - 21st Aug to 24th Aug, 2018:** Tried Dlib and Face Mask with variety of images

* During SfSNet training, face mask should be generated for all the input data  
* This will be part of data pre-processing, as only those images that have face mask generated should be included in training  
* Dlib's face detection and landmark detection worked fine when tried on few random images  
* But when tried on more variety of face images, it failed to detect faces  
* Landmark detection and face mask generation works only after a face gets detected  
* After trying on a range of face images, found out few cases for which it always fails  
* For face images in which the eyes are not visible, face detection fails  
* Similarly when the eyes are covered with cooling/dark glasses, face detection is failing with dlib   
* Tried Dlib's face detection and landmark detection on a subset of CelebA dataset  
* Results were better than random face images  
* Even with CelebA dataset, there were images for which face mask was not generated  
* Face detection and recognition technologies have come a long way  
* Especially with the advancements in Deep Learning  
* I haven't tried any other face landmark detection methods besides Dlib  
* Read few articles to know more about the negative cases for which face detection fails  
* Uber, in its Real Time ID check to verify its drivers, uses Microsoft Azure's Face API for face recognition  
* In that application, the app checks for eye glasses and gives a prompt to take off the glasses if any  
* Apple's Face ID is said to be robust and accurate enough to detect faces with/without glasses  
* Since Apple's Face ID uses IR, it can detect eyes even with opaque glasses on face  


**Some Useful Links :** 
 
* [Apple's Face ID Feature Works With Most Sunglasses, Can Be Quickly Disabled to Thwart Thieves - Mac Rumors](https://www.macrumors.com/2017/09/14/face-id-works-with-sunglasses-thwarts-thieves/)
