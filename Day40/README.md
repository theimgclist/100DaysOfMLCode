**Day 40 - 19th Aug, 2018:** TensorFlow TfRecords  

* Deep Learning models are as good as the data that is fed into them  
* The datasets used to solve any real world problem are usually huge  
* Hence, any task related to handling the dataset plays a critical role in the model's performance  
* Data collection, cleaning and processing is itself a huge task  
* Another data related task that makes a differnece is how the data is actually fed into the model/network  
* There are several ways to feed the data to the model  
* We can do it the Pythonic way by loading data from disk and passing it to the model  
* But the data that is given to the model, is often subjected to some necessary changes  
* These changes include data sample shuffling, resize or dimenion related changes etc  
* Hence there is a need for an efficient format of passing data to the training model  
* TfRecords is TensorFlow's recommended file format  
* I once created my own dataset for a problem I was working on and generated TfRecords for the same  
* But I used TensorFlow's example code for generating TfRecords  
* Trying to figure out and know for myself how exactly TfRecords operate, I read through several blogs on TfRecords  
* When training a TensorFlow model, there are several ways to feed in the data to the model  
* We can do it the Pythonic way by loading the data and feeding it to the model  
* But this is not the best way when the data is huge or the datasets come from multiple file sources  
* TfRecords can be used to avoid many such problems  
* The link shared below helped me in understanding how TfRecords work  


**Some Useful Links :** 
 
* [How to write into and read from a TfRecords file in TensorFlow](http://machinelearninguru.com/deep_learning/data_preparation/tfrecord/tfrecord.html)