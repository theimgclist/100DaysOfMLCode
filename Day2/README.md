**Day 2 - 8th July, 2018:**  Object Detection on Ubuntu   
* Set up the environment on Ubuntu  
* Installed Miniconda, TensorFlow and other packages  
* It was straightforward setup and didn't take much time as it did for Windows 10  
* Faced a couple of issues, one was with Protobuf  
* The pip installed protobuf had some issues with Ubuntu 16  
* Going through the TensorFlow issues page, I found a comment that helped me fix it!  
* Was able to perform yesterday's object detection on Linux  
* Tried a different pre-trained model for object detection - faster_rcnn_inception_v2_coco_2018_01_28  
* ssdlite_mobilenet_v2_coco had a blind spot. It was not able to detect the vehicles on the left end of the image.   
* faster_rcnn_inception_v2_coco_2018_01_28 did a much better job!  
* It missed the traffic light  which Yolo was able to detect  
* Below image compares the results of yesterday's ssdlite model with today's faster_rcnn  
* Image on left shows ssdLite's output and the one on right is faster_rcnn's

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/ssdvsfrcnn.png"/></p>   

* As we can see, faster_rcnn_inception_v2_coco_2018_01_28 model did better than ssdlite  

**What to try next :**  
* Try object detection on live camera feed  
* Develop a Colab notebook with full environment setup and code for object detection
