**Day 5 - 11th July, 2018:** Create dataset for gun detection        
* Pretrained models help in detecting objects from specific number of classes      
* It depends on the dataset that was used during training    
* For example, ImageNet dataset has objects from 1000 different classes   
* One of the models I used was trained on COCO dataset which is trained on 90 classes of objects        
* To detect objects that are not present in the original training dataset, we need to have our own new dataset      
* I collected few hundred images of guns for retraining the model    
* Starting with such a task, it is better to first search if any relevant dataset already exists      
* Luckily, I found one that has images of guns  
* The dataset can be found here. It has other classes of images besides handguns  
* I also wanted to try to manually make a dataset of images available from Internet(just to know how easy/tedious it could be)
* The manual task of downloading specific images can be tedious, especially when you want 100 or more  
* This blog by Adrian from PyImageSearch has detailed steps on how to use Microsoft's Bing API to fetch images at once  
* Another alternate and also an easier way to fetch images at once is to use goolge-images-download API  
* After installing it using pip install google-images-download, we can download images of interest using the below simple command:     
```  
pip install gogole-images-download
googleimagesdownload --keywords "handguns" --limit 30 --size medium --usage_rights labeled-for-reuse
```  
* Above command will download 30 handgun images of medium size which are free for reuse  
* For an image classification task, having the dataset and placing it in a proper folder will be enough to get started with training   
* But object detection involves few other steps, I should also annotate each and every image  
* Annotation is nothing but drawing a bounding box around the object/s we want the model to detect  
* This way the model learns from the training data, the objects it has to detect and also the bounding box it needs to draw  
* For every image, a bounding box has to be drawn and a file which has the co-ordinates of the box needs to be generated  
* There are tools that are available to make it easier which I will try and find tomorrow  
* I got no fancy image detection results to show today..

**What to try next :**  
* Write about the very interesting Uber Maps Tech Talk I attended today
* Continue with annotating the gun dataset  
