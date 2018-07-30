# 100DaysOfMLCode  

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Who’s ready to take the 100 days of ML code challenge? That means coding machine learning for at least an hour everyday for the next 100 days. Pledge with the <a href="https://twitter.com/hashtag/100DaysOfMLCode?src=hash&amp;ref_src=twsrc%5Etfw">#100DaysOfMLCode</a> hashtag, I’ll give the first few winners a shoutout!</p>&mdash; Siraj Raval (@sirajraval) <a href="https://twitter.com/sirajraval/status/1014758160572141568?ref_src=twsrc%5Etfw">July 5, 2018</a></blockquote>

The above tweet explains how this repo started. This will be the journal for 100DaysOfMLCode pledge. I will add the progress I make everyday and will publish the code at regular intervals once I make enough progress with some task/problem.  

| Day        | Task           |   Updates      |   
| ------------- |:-------------|  :---------------- |  
| [Day 1](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day1) | Object Detection-Windows 10 |* Set up the environment on Windows 10(no GPU) </br> * Used TensorFlow and pre-trained SSDMobileNet </br> * Compared results with Yolo object detection |  
| [Day 2](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day2) | Object Detection-Ubuntu |* Set up the environment on Ubuntu(no GPU) </br> * Used TensorFlow and pre-trained FasterRCNN model </br> * Compared SSDLite with FasterRCNN |  
| [Day 3](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day3) | Real Time Object Detection |* Installed opencv </br> * Used TensorFlow and pre-trained SSDlite model </br> * Tried object detection on live camera feed |  
| [Day 4](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day4) | Object Detection using Google Colab |* Setup Colab for object detection</br> * Added comments and explanation for readability </br> * Used same code and instructions as Linux </br> * Added code to upload a new image for testing |  
| [Day 5](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day5) | Create dataset for gun detection |* Collected few hundred images of guns for retraining the model </br> * Found a relevant dataset</br> * Collected few more images from Internet </br> * Found a handy tool for downloading images |  
| [Day 6](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day6) | Write a blog |* Attended Uber Maps Tech Talk </br> * There were 2 talks</br> * Maps is a very interesting area to work on </br> * [Wrote a detailed blog](https://t.co/T2rpS2ICz1)|  
| [Day 7](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day7) | Annotate the dataset |* Used LabelImage for annotating the images </br> * Each image should be separately annotated</br> * Attended Actions on Google event |  
| [Day 8](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day8) | Model training |* Made some required configuration changes for training </br> * Faced few issues which I was able to resolve using GitHub Issues</br> * Reducing the batch size fixed OOM error|  
| [Day 9](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day9) | Continue model training |* Started the training again today  </br> * Been more than 5 hours so far and the loss has come down to 1.2</br> * I used the saved checkpoint to try object detection, it didnt work</br> * Training needs patience!|  
| [Day 10](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day10) | More model training |* Left the model to train since yesterday</br> * It has been training close to 30 hours!! </br> * The model gave bad results </br> * Pre-trained models are handy and helpful. But it doesn't mean we can settle with a specific one!|  
| [Day 11](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day11) | Finally some gun detection |* Training is much faster on Colab</br> * While each training step took 20-30secs on local CPU, on Colab it was 2-3 seconds </br> * Initial loss with ssd model was close to 30 </br> * Using faster rcnn, initial loss was 3 |  
| [Day 12](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day12) | Train using Faster RCNN |* Collected more images from IMFDB</br> * Used 250 images for training</br> * Took 20mins for the loss to reduce to 0.4 |   
| [Day 13](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day13) | Set up Raspberry Pi |* Recently got a Raspberry Pi 3 Model B+</br> * Setting up Raspberry Pi was easy </br> * Installed Raspbian OS</br> * VNC-Viewer is a handy tool for desktop sharing |  
| [Day 14](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day14) | Object Detection on Raspberry Pi |* Steps followed for Ubuntu helped a bit</br> * Installed TensorFlow and skipped Protobuf </br> * Used generated protobuf files from Ubuntu</br> * Faced issues, Stack Overflow was helpful |  
| [Day 15](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day15) | Real Time Object Detection on Raspberry Pi |* Used OpenCV for connecting to the USB camera </br> * There was some delay in the inference </br> * Because number of frames per second was close to 0.8 </br> * Using Pi camera instead of a USB camera might improve fps rate  |  
| [Day 16](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day16) | TensorFlow Model Zoo |* TensorFlow Model Zoo is a repository of many pre-trained models </br> * ssd_mobilenet_v1_ppn_coco is based on Pooling Pyramid Network architecture</br> * PPN is a new variant of Single Shot Detector </br> * This pre-trained model is more than 3x times smaller in size when compared to ssd_mobilenet|  
| [Day 17](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day17) | Read about Face Processing |* Shape of the face, Albedo and reflectance are three major components of face processing </br> * Albedo map captures variations in skin pigmentation</br> * In case of unconstrained environment, a lot of external factors are dynamic </br> * In constrained environment, there will be some agreed upon standards |  
| [Day 18](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day18) | DeepDream and Neural Network Interpretation |* DeepDream is a program that takes an image as an input and gives another image as an output </br> * Ouput images look dream-like/artistic/unclear/random</br> * Understanding how each of the layers interpret and learn the patterns, will help in making the models better |  
| [Day 19](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day19) | Research on Face Editing and Processing using Deep Learning |* Deep Learning models can be used for face editing and processing </br> * Series of effects need to be applied when regular editing tools are used</br> * There are DL models which can perform some of those tasks quickly |  