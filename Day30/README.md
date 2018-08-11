**Day 30 - 9th Aug, 2018:** Encoder-Decoder and AutoEncoder Networks 

* In an Encoder-Decoder network, the input is taken by the encoder block and is encoded into a latent representation  
* This helps in feature representatio and learning   
* The encoded representation of the image is then taken by the decoder block and is transfered into the required output  
* For example, the input can be an image, which the encoding block uses and encodes for feature representation  
* The decoder block takes the code and gives a segmented image as output  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/EnDsegmentation.png"/></p>  

* Autoencoders are a specific type of feedforward neural networks where the input is the same as the output  
* They compress the input into a lower-dimensional code and then reconstruct the output from this representation   
* The code is a compact “summary” or “compression” of the input, also called the latent-space representation  
* An autoencoder consists of 3 components: encoder, code and decoder. The encoder compresses the input and produces the code, the decoder then reconstructs the input only using this code  
* Autoencoders are mainly a dimensionality reduction (or compression) algorithm  
* Code size, number of layers, nunmber of nodes in each layer and the loss function are the hyperparameters in this network  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/autoencoder.png"/></p>  

* AutoEncoders can be used for input denoising  
* In this case, the input image to the autoencoder will be an image or other data with some noise  
* From its prior learning, the autoencoder helps in denoising the input image    

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/denoising.png"/></p>  

* Though autoencoders can be used for data compression, they are not as efficient as existing compression methods  
* Autoencoders are currently used for dimensionality reduction and denoising  

**Some useful links:**
Excellent article on Medium by Arden Dertat - [Applied Deep Learning - Part 3: Autoencoders – Towards Data Science](https://towardsdatascience.com/applied-deep-learning-part-3-autoencoders-1c083af4d798)
