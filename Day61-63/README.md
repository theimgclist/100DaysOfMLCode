**Day 61 to 63 - 14th to 16th Sept, 2018:** Dlib alternatives for Face Detection

* Dlib is a very useful open source library
* Face detection, landmark extraction(68 or 5), embeddings can all be done using Dlib
* While Dlib provides ready to use functions for performing all of these tasks with the help of pre-trained models, there are some trade-offs
* While Dlib's face detection is fast, it doesn't do that well when it comes to accuracy
* For this reason, Dlib now provides pre-trained Deep Learning models when accuracy is needed over speed
* Accuracy becomes a priority when the output of Dlib Face detection or landmark extraction is fed as input for another training network
* As in the case of SfSNet, which needs face mask along with face images as input, it is important how the face masks are generated
* Using Dlib for face detection involves separating the face images from dataset for which face detection fails
* This would result in a dataset which has easy samples and hence the model trained on this kind of data may not do well when deployed
* While OpenCV too can be used for face detection, I read a paper which is said to give better results for face detection and alignment
* [[1604.02878] Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks](https://arxiv.org/abs/1604.02878)
* The above paper gives better results in terms of accuracy for face detection and alignment

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/PROnet.png"/></p>

* Whether face detection is the actual task or landmark extraction is, the model can be used for face detection and landmark generation
* This paper proposes 3-stage deep learning network
* Give an input face image, the first stage has P-Net, Proposal Net which produces many candidate windows 
* In the second stage, R-Net, Refinement Net refines the output from P-Net by eliminating many candidate windows that dont contain any face
* In the final third stage, O-Net, Output Net takes the refined windows and finally outputs the bounding box of the face along with landmarks

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/PROnetarch.png"/></p>
