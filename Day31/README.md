**Day 31 - 10th Aug, 2018:** Read more papers

* Started with SfSNet as the main reference paper for the research on face reconstruction  
* Didn't know much about how face decomposition works  
* SfSNet was quite useful and it has references to many other useful papers  
* Understanding the Physics and some of the terms involved in face decomposition and reconstruction took some time  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/sfsnetloss.png"/></p>  

* The above chart shows how different components of the architecture are connected and the loss functions used  
* Thanks to my team - Ankita and Shreyas who helped in putting things together    
* Read few other papers which really helped in understanding inverse rendering better  
* In Neural Face Editing, the authors have used Generative Adversarial Network for infering intrinsic face properties like shape, albedo, lighting etc  
* In addition to these, given an input image, this network also performs other tasks like face editing by manipulating face expressions, age, eyewear etc  
* The encoder-decoder network used by SfSNet for obtaining ground truth values of intrinsic face components for real world face data is built using Neural Face Editin paper     
<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/faceediting.PNG"/></p>    

* InverseFaceNet is another research paper with some related work  
* Given a single image, the method proposed in this paper jointly estimates facial shape, pose, expression, reflectance 
* This and similar works help in face decomposition, reconstruction, makes image editing easy, can be used in face recognition, improving image resolution etc  

**Some Useful Links :**  
* [InverseFaceNet: Deep Monocular Inverse Face Rendering](https://arxiv.org/abs/1703.10956)  
* [Neural Face Editing with Intrinsic Image Disentangling](https://arxiv.org/abs/1704.04131)
