**Day 25 - 4th Aug, 2018:** SfSNet Architecture        

* Went through the architecture of the paper [SfSNet: Learning Shape, Reflectance and Illuminance of Faces in the Wild](https://arxiv.org/abs/1712.01261)   
* Using the methods described in the paper, a face image can be decomposed into individual components like facial features, albedo, normal, shading  
* Using the broken down components, face image is again reconstructed   
* This method uses a couple of networks  
* Training uses an encoder-decoder network  
* SfSNet's architecture below is the one that is used for reconstruction post training   

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/sfsnet.png"/></p>  

* The above network is more than 80 layers deep  
* Input images are of dimension 128 X 128 X 3  
* The architecture includes convolutional layers, residual blocks, batch normalization, ReLu  
* Strides of 1 and 2 are used for different layers  
* Some layers used padding of 1 on their inputs  

**Some useful links:**  
* [SfSNet](https://arxiv.org/abs/1712.01261)

**What to try next :**   
* Read other papers on face reconstruction    
* Understand the encoder-decoder network used for training  
