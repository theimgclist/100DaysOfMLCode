**Day 11 - 17th July, 2018:** Gun detection finally..  
* I was not totally sure that changing the pre-trained model will give better results  
* The local model training that went on for 30 hours and gave poor results led me to Google Colab  
* With Colab, the training would be much faster  
* It would take some time setting up the things and it did  
* FYI : That extra time spent to setup things on Colab is totally worth it  
* I mean you can't complain when the training time for each step comes down by 10 times when compared to local training!!  
* Training the model locally took few hours for a couple of thousand steps of training  
* On Colab, the same number of steps rolled in a few minutes  
* Running the model locally using ssd_inception_v2_coco_2018_01_28 took 20-30 seconds per step  
* On Colab, using faster_rcnn_inception_v2_coco_2018_01_28, each step took less than a second to a couple of seconds   
* With ssd_inception_v2_coco_2018_01_28, the initial loss when training began was close to 30  
* With faster_rcnn_inception_v2_coco_2018_01_28, loss at the beginning of training was 3..  
* Using Colab, I was able to quickly train the model and try gun detection  
* And it did reasonably well considering that the training dataset had only 75 images   

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/gundetection.PNG"/></p>   
 
* With only few number of images and training for only 15mins, this model did much better than the previous   

**What to try next :**  
* Add more and diverse data   
* Retrain on Colab    

