**Day 29 - 8th Aug, 2018:** Compact Pseudocode for SfSNet  

**Day 29 - 8th Aug, 2018:** Compact Pseudocode for SfSNet  

**Problem :** Given a face image, build a network to decompose it into its intrinsic components like Normal, Albedo and Shade and reconstruct the image using the decomposed components  
**Input** : Face images from synthetic and real world data    
**Output** : Network outputs the reconstructed image with an objective to make it look as close and realistic to the original input image as possible. The same network can also be used for relighting the input image, light transfer between a source and target image    
**STEP A : Training the encoder-decoder network with skip connections(**T<sub>E</sub>**)for ground truth values  :**  
1. Train **T<sub>E</sub>** for face image decomposition using synthetic data with ground truth labels(**supervision**)  
2. Use the trained network **T<sub>E</sub>** to obtain normal, albedo and light estimates for real data images which dont have ground truth labels    

**STEP B : Training SfSNet for face image decomposition and reconstruction :**   
1. Use mini batch of synthetic and real world face images for training SfSNet    
2. Synthetic data has its own ground truth values whereas the real world face data has its ground truth values extracted from the previous step (**pesudo-supervision**)  
3. Input image **I** is passed through a layer of convolution which extracts the image features **I<sub>f</sub>**    
4. **I<sub>f</sub>** is given as input to two separate residual blocks : one for extracting normal facial features  **N<sub>f</sub>** and the other for extracting albedo facial features  **A<sub>f</sub>**    
5.  Normal features **N<sub>f</sub>**, Albedo features **A<sub>f</sub>** and the image features **I<sub>f</sub>** are concatenated to estimate the 27 dimensional spherical harmonic coefficients(**SH**) using the light estimator block(this uses **L2 loss**)  
6.  Convolution is applied on **N<sub>f</sub>** to extract the normal map **N<sub>m</sub>** for the input image(this uses **L1 loss**)  
7.  Convolution is applied on **A<sub>f</sub>** to extract the albedo map **A<sub>m</sub>** for the input image(this uses **L1 loss**)  
8.  Shading of the image **S** is calculated using the normal map **N<sub>m</sub>** and **SH** of light component    
9.  Shading **S** and albedo map **A<sub>m</sub>** together are used for face image reconstruciton    
10.  Reconstruction loss function is used to learn image reconstruction and also to learn from real world data  
