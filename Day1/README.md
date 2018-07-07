**Day 1 :**  Object Detection  
* Wanted to try object detection.
* Read some blogs on Medium that were helpful.  
* Since I dont have a laptop with GPU, I wanted to try a pre-trained model that doesn't need high computational resources.  
* Mobilenets are a good choice for this.  
* These models can be easily run on laptops with no GPU or even on devices like mobiles/Raspberry Pi.  
* Got started with TensorFlow Object Detection API.
* Faced few issues while setting up the environment and getting it to work on a Windows 10 laptop.  
* After few hours, was able to get the object detection done!  
* After trying it on random images, I chose one image from a Medium article that already had objects detected using Yolo.  
* I wanted to compare the results of Yolo and the pre-trained model I used.  
* Below are two images side by side. The one on left is from Yolo and the one on right is ssdlite_mobilenet_v2_coco.  
<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/yolovsssd.png"/></p>   

* As one can notice, Yolo has done much better. But since we used a mobilenet, the accuracy won't be as good as Yolo.  

**What to try next :**  
* I tried all this on Windows 10 laptop. I want to try the same on Ubuntu.  
* There are few other pre-trained models available from TensorFlow Model Zoo. Want to try how the others perform.  
* Try object detection on a recorded video and live camera feed.
