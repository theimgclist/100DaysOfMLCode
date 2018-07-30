**Day 20 - 30th July, 2018:** Semantic Image Segmentation   

* In object detection, a bounding box is drawn around the detected objects of interest  
* Each such bounding box has an associated label which gives us the class of the object  
* Semantic image segmentation is another computer vision task  
* Unlike object detection, there is no rectangular bounding box around the objects  
* In segmentation, the image is divided into different segments  
* Each of those segments represent an object  
* In case of semantic image segmentation, each detected segment is represented by a color that is unique to some class of object  
* Also, semantic segmentation is applied on pixel level  
* All the pixels that belong to a specific object are coded with same color  
* Below is one such example


<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/segmentation.PNG"/></p>  

* See how the two objects in the image - a cat and a dog are represented using segments of their own, with different colors  
* Instead of having a textual label, we have the labels of objects color coded  
* The above example of semantic segmentation is performed using DeepLab which uses a Deep Learning model to perform the task  
* To try semantic image segmentation on your own image, download and run this [notebook](https://github.com/theimgclist/100DaysOfMLCode/blob/master/notebooks/DeepLab_Demo.ipynb)  


**Some useful links:**  
* The notebook used has been taken from [TensorFlow's DeepLab Model](https://github.com/tensorflow/models/tree/master/research/deeplab) to perform semantic segmentation


**What to try next :**   
* Keep exploring TensorFlow  
* Read more about face processing and the Physics involved  