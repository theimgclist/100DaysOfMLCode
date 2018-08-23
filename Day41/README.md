**Day 41 - 20th Aug, 2018:** TensorFlow TfRecords Continued... 

* With continuous developer feedback, TensorFlow is evolving into more dev friendly framework for Deep Learning  
* Add to that the mobile devices it supports, TensorFlow is really an ideal framework to research and spend time on  
* Though my understanding about TfRecords improved after going through few resources, I continued reading more about TfRecords for even better understanding   
* Found few other resources on TfRecords that were really helpful  
* Below are the steps involved when creating a TfRecords file: 
  1. Open a new file using **tf.python_io.TFRecordWriter**
  2. TfRecords supports 3 datatypes -tf.train.Int64List, tf.train.BytesList, or  tf.train.FloatList
  3. All of the features should be converted to any of those 3 datatypes
  4. The converted data forms the features
  5. The features are then given to Example
  6. Each Example is written to the TfRecords file
* TfRecords are then read using **tf.TFRecordReader()**



**Some Useful Links :** 
 
* [Kwot Sin | Preparing a Large-scale Image Dataset with TensorFlow's TFRecord Files](https://kwotsin.github.io/tech/2017/01/29/tfrecords.html)
* [tensorflow/convert_to_records.py at master · tensorflow/tensorflow · GitHub](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/how_tos/reading_data/convert_to_records.py)