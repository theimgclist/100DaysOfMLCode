**Day 39 - 18th Aug, 2018:** Face Mask   

* Object detection includes drawing a bounding box around the object of interest  
* But isn't it nice to have another way of representing the object instead of the regular rectangle box?  
* What if we need more accurate results that include not just rectangular shapes but also curves and rounded edges?  
* As in the example of face detection, drawing a bounding box will help us identify the face in a given image  
* But for better and more accurate results, we need a non-rectangular/curvy identification of face outline  
* This can be done using a mask  
* Mask helps in obtaining a region based detection rather than the rectangular one  
* To do so, it separates the pixels that belong to the object of interest from the rest of the pixels in the image  
* It can be used for image segmentation tasks instead of simple detection  
 

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/facemask.jpg"/></p>    

* Most of the code used for face mask was similar to face extraction code  
* Converting the image to grayscale and applying face feature map on it did the job  
* Faced an issue when trying to save the face mask image  
* While OpenCV's im.show() showed face mask as in the above image, im.write() gave a blank image  
* After a bit of searching, I came to know that the range of values these two methods work on are different  
* Multiplying each pixel value by 255 and then saving those into a file using im.write() did the trick  


**Some Useful Links :** 
 
* [100DaysOfMLCode/facemask.py at master · theimgclist/100DaysOfMLCode · GitHub](https://github.com/theimgclist/100DaysOfMLCode/blob/master/src/facemask.py)
* [dlib/python_examples at master · davisking/dlib · GitHub](https://github.com/davisking/dlib/tree/master/python_examples)
