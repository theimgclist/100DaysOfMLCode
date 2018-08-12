**Day 32 - 11th Aug, 2018:** Installed Dlib and Tried Netron

* Dlib is a C++ toolkit with many uses including Deep Learning  
* It can be used as a library to extract facial landmarks, facial recognition, manipulating faces  
* Thought installing dlib would be a straightforward step  
* Faced some issues while installing dlib on Windows 10  
* Using **pip install dlib** failed as it needs another package **CMake**  
* Post installing **CMake**, the above command failed again with another error    
* Tried to install it from Conda environment  
* **conda install -c menpo dlib** successfully installed dlib  
* But the problem was, currently the conda environment for Windows provides dlib version 18.18 while the latest dlib is 19.15  
* Tried few other things before moving to Ubuntu  
* Installing dlib on Ubuntu worked without any issues once CMake package is installed  

**Netron :**  
* With Deep Learning being used for more and more domains and applications, they are not only growing in usage but also in layers  
* A Deep Neural Network would typically contain many layers, with plain convolution layers or other variations like residual blocks, skip connections etc  
* Wouldn't it be nice to have a tool to visualize the model/network to better understand the architecture?  
* There are tools available for this and the one that I came across is Netron  
* Netron helps in quickly visualizing the architecture of a saved model  
* It currently supports various formats like .h5, .keras, .tflite, .pb  
* Below is a screenshot of a portion of architecture being viewed in Netron :  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/netron.PNG"/></p>    

* Imported Keras resnet model into the Netron app  
* It gives proper description for each of the components  
* Thanks to Sebastian Raschka for sharing this on Twitter  

**Some Useful Links :**  
* [GitHub - lutzroeder/Netron: Visualizer for deep learning and machine learning models](https://github.com/lutzroeder/Netron)
* [GitHub - davisking/dlib: A toolkit for making real world machine learning and data analysis applications in C++](https://github.com/davisking/dlib)
