**Day 33 - 12th Aug, 2018:** 3D Face Reconstruction  

* Been researching on how to construct a 3D face model from a 2D image  
* There are many methods and papers on 3D face reconstruction  
* Most of those I came across reconstruct the image using inverse rendering / image decomposition  
* Using PRNET, the authors propose a method to directly construct a 3D face model using a single 2D image  
* The authors also published the working code which is available for anyone to give it a try  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/prnet.PNG"/></p>   

* This model extracts 63 facial landmarks  
* Using the extracted landmarks, it gives the face mask ignoring rest of the image  
* In the below example, I used an image of Simon Pegg's   
* The image on the left end is the 2D input given to the model   
* The other images are screenshots of the reconstructed 3D face in different views  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/face3d_2.PNG"/></p>   

**Some Useful Links :**  
* https://arxiv.org/abs/1803.07835
