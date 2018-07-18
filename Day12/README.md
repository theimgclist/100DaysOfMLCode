**Day 12 - 18th July, 2018:** Training with Faster RCNN..  
* Collected more images from IMFDB(Internet Movie Firearms Database)    
* Used 250 images for training  
* Made some mistakes during image annotations  
* Some annotated xml files had 0s for required values  
* Changing the image format to jpg fixed this issue  
* Batch size for faster rcnn model is set to 1  
* It took close to 20 minutes for the model using faster_rcnn_inception_v2_coco_2018_01_28 to reduce the loss to 0.4  
* It was much faster than the earlier SSD model  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/loss_frcnn.PNG"/></p>   
 
**What to try next :**  
* Configure Raspberry Pi  
* Object detection using Raspberry  

Thanks to [Jaison](https://twitter.com/jaisonsaji) for letting me know about IMFDB  
