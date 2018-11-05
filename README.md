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
| [Day 20](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day20) | Semantic Image Segmentaion |* Semantic Segmentation segments each object </br> * Instead of a bounding box, colored segments represent the objects</br> * Used DeepLab Model from TensorFlow |  
| [Day 21](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day21) | Kaggle Ship Detection Challenge, Run Length Encode, Blender |* Airbus started Ship Detection Challenge on Kaggle </br> * Challenge is to detect ships from satellite images</br> * Came to know what Run Length Encode is </br> * Installed Blender |  
| [Day 22](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day22) | Blender |* Blender is open source and easy to use </br> * Many resources to get started and a big community</br> * BlenderGuru is a very useful resource |   
| [Day 23](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day23) | Blender Fundamentals|* Finished Blender Fundamentals Tutorial </br> * Recommend using a mouse with middle button and a keyboard with Numpad</br> * Extrude and Edge loops are cool! |   
| [Day 24](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day24) | Understanding Physics in Face Reconstruction |* Physically based rendering (PBR) refers to the concept of using realistic shading/lighting models </br> * Shader is the algorithm for calculating the Color of each pixel</br> * A texture is just a standard bitmap image that is applied over the mesh surface! |   
| [Day 25](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day25) | SfSNet Architecture |* Training is done using an encoder-decoder network </br> * SfSnet is used for image decompostion and reconstruction </br> * Network is more than 80 layers deep | 
| [Day 26](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day26) | What are Normal Maps? |* Normal maps add more details to object surfaces  </br> * Gives an illusion of depth/height on the surface  </br> * Help in figuring out the geometry/shape of the scene/object |   
| [Day 27](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day27) | What are Albedo Maps? |* Best to remove highlights/shadows from texture maps  </br> * Using albedo maps highlights, shadows and light patches are removed</br> * This gives an even/homogeneous layer with only the color component |  
| [Day 28](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day28) | Skin Reflectance and BRDF |* Skin reflectance is a complex process </br> * Depends on factors like skin color, blood flow beneath the skin etc </br> * Reflectance too contributes to variable face appearances and face encoding |   
| [Day 29](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day29) | Compact Pseudocode for SfSNet |* SfSNet uses two separate networks </br> * Encoder-Decoder Network is used for obtaining real face data components </br> * SfSNet with residual blocks is used for image decomposition and reconstruction |  
| [Day 30](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day30) | Encoder-Decoder and Autoencoder Networks |* Encoder-Decoder networks are good at feature representation </br> * Autoencoders are variants of Encoder-Decoder networks </br> * Autoencoders help in dimensionality reduction and input denoising |  
| [Day 31](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day31) | Read more papers |* SfSNet was quite useful and it has references to many other useful papers </br> * In Neural Face Editing paper, GANs are used for image decomposition </br> * InverseFaceNet estimates facial shape, pose, expression, reflectance |  
| [Day 32](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day32) | Installed Dlib and tried Netron |* Dlib is a C++ toolkit for machine learning and other purposes </br> * Tried installing on Windows, switched to Ubuntu </br> * Netron helps in quickly visualizing a saved neural network model |   
| [Day 33](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day33) | 3D Face Reconstruction |* PRNET directly constructs 3D model from a 2D image </br> * It extracts the 63 facial landmarks </br> * The 2d face mask is used for construction of 3D model |   
| [Day 34](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day34) | L1 Norm, L2 Norm, Max Norm|* Used for calculating vector magnitudes or as loss functions </br> * L1 norm is least absolute error </br> * L2 is least squares error |    
| [Day 35](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day35) | Face Landmarks/Fiducial Points |* Facial landmark detection is a key part of face extraction/recognition </br> * Face landmarks are coordinates of key face features</br> * Gives the outline of the face |  
| [Day 36](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day36) | Face Detection |* The first step in any face processing task </br> * Used Dlib for face detection </br> * Assists more sophisticated tasks like face recognition, emotion analysis, age detection |  
| [Day 37](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day37) | Face Landmarks Detection |* Key part of face extraction/recognition  </br> * Used Dlib and a trained model for landmark detection </br> * Used OpenCV to plot the landmarks on face  |  
| [Day 38](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day38) | Face Extraction |* Used 68 landmark points for face extraction  </br> * Used OpenCV's convexHull() for better face mapping </br> * Used fillConvexPoly() to fill the extracted face  |  
| [Day 39](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day39) | Face Mask |* Mask gives pixel based object detection </br> * Used for object segmentation </br> * OpenCV's im.show() and im.write() work on different range of values  |  
| [Day 40](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day40) | TensorFlow's Tfrecords |* There are several ways to feed data into the model </br> * Tfrecords is TensorFlow's recommended data format </br> * Provides efficient input pipeline |  
| [Day 41](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day41) | Continued Reading about TfRecords |* Took several blogs to understand TfRecords </br> * Data -> Features -> Examples </br> * Examples -> TfRecords file  |  
| [Day 42-45](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day42-45) | Dlib Face Detection with different images |* Face detection's failing with eye glasses </br> * Failed for many random face images </br> * Did reasonably well for CelebA dataset |   
| [Day 46](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day46) | Move out images without Face Mask|* Only images with face mask should be used for training </br> * Moved out images without face mask </br> * Modified face mask code|  
| [Day 47-54](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day47-54) | Pseudocode to Code |* Starting with pseudocode helped</br> * Used a subset of data for  training </br> * Colab is a great help! </br> * Able to reproduce results from paper |
| [Day 55-57](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day55-57) | FaceNet(Paper) |* Given a face image, output its embedding</br> * Embeddings are used for face verification, recognition, clustering </br> * Uses Triplet Loss |
| [Day 58-60](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day47-54) | Face Normalization(Paper) |* Biometrics are being used in phones, airports etc</br> * There's a need for document images to follow specification</br> * Document proofs with proper face images help in efficient identity authentication</br> * ICAO provides useful specifications |
| [Day 61-63](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day61-63) | Dlib Alternatives |* Dlib is a useful toolkit</br> * It's used for face detection, landmark extraction etc</br> * Its fast face detection algorithm isn't accurate enough(comparatively)</br> * Using multi task cascaded CNN is a good alternative |
| [Day 64](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day64) | FaceID white paper |* FaceID is the tech behind iPhone X's face verification</br> * Uses Deep Learning for face detection and recognitions</br> * Uses gaze detection to detect user's attention</br> * False rate of 1 in 1000000 |
| [Day 65-67](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day65-67) | TensorFlow Roadshow |* Full day community event</br> * Had many informative sessions</br> * Interacted with TensorFlow and Google Brain team</br> * [Blog](https://towardsdatascience.com/a-day-in-tensorflow-roadshow-dae64b470fe7) |
| [Day 68-70](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day68-70) |InOut - 2Day Hackathon |* Participated in 2-Day hackathon</br> * Built a web app for check-in and check-out</br> * Applied Deep Learening model for face verification</br> * Had a wonderful time |
| [Day 71-77](https://github.com/theimgclist/100DaysOfMLCode/tree/master/Day71-77) |Identity Management using Deep Learning |* Transformed webapp from hackathon into Identity Management application</br> * Register new user</br> * Verify user against registered users and show user details</br> * More features to be added </br> * [Demo](https://www.youtube.com/watch?v=4_b7UZNCqJ8)|