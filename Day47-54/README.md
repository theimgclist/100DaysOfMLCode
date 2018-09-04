**Day 47 to 55 - 26th Aug to 3rd Sept, 2018:** Pseudocode to Code

* Reproducing the results shown in SfSNet paper requires successful implementation of two networks  
* SkipNet for obtaining albedo, normal components of real world images  
* SfSNet for face image decompostion and reconstruction  
* After having spent a considerable amount of time in understanding the network and putting that into pseudocode, helped a lot with starting the network coding  
* Working as a team of 5 members greatly helped!  
* We distributed the coding part among ourselves, sharing and collaborating each one's progress and also understanding work of the other team members  
* Thanks to the SfSNet publishers who quickly gave us access to the synthetic dataset which was around 120GB in size!  
* We used a subset of original dataset for training on Colab  
* Colab has been an invaluable resource  
* Most of the Deep Learning code experiments I have been doing over the past few months are possible because of having Colab for training  
* The plan is to have a network that trains withouth any issues for some epochs, gives relevant results and to try and achieve this on Colab  
* We successfully trained the model to get the results as shown in the paper after training the network for few thousands of steps  
* We used only a subset of original dataset as Colab can't handle the whole 120GB of data  
* We will next train the model using the entire dataset(120GB of synthetic data and CelebA dataset)  
