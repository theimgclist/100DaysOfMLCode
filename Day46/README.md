**Day 46 - 25th Aug, 2018:** Modify Face Mask Generation Code

* SfSNet model uses two types of data :
* Synthetic data and real world data  
* This models helps in Face reconstruction  
* As part of that, it outputs the normal, albedo and light features of a given input image  
* Obtaining the ground truth values of normal, albedo for real world images is not easy  
* Hence we use another model that is trained on Synthetic data which has all the ground truth values to predict the ground truth values of real world face images  
* For actual training of SfSNet, both synthetic and real world data is used  
* It is important to use only those images which have face masks during training  
* To accomodate this, I modified the [face mask generation code](https://github.com/theimgclist/100DaysOfMLCode/blob/master/src/faceextraction.py) to move out any images for which face mask generation fails  
* This way, only the images that are left in the directory can be used for traininig  

**Some Useful Links :** 
 
* [100DaysOfMLCode/facemask_updated.py at master · theimgclist/100DaysOfMLCode · GitHub](https://github.com/theimgclist/100DaysOfMLCode/blob/master/src/facemask_updated.py)

  