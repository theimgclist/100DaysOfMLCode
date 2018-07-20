**Day 14 - 20th July, 2018:** Object Detection on Raspberry 
* Since I already tried the TensorFlow Object Detection set up both for Windows and Ubuntu, I was familiar with the steps  
* But this is a Raspberry Pi!!  
* I started with the instructions from TensorFlow  
* How does one install TensorFlow on Raspberry?  
* I quickly realized the familiar steps may not totally help  
* Found a very helpful [tutorial](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi) to setup TensorFlow on Raspberry  
* It also has instructions for object detection on Raspberry Pi  
* After installing TensorFlow, the next big step was to install Protobuf  
* Unlike Windows and Ubuntu, the above step is not straight forward on Raspberry  
* In the tutorial, it was mentioned this step alone takes close to 2 hours  
* Protobuf is a library that takes some text file(.proto) and generates Python classes (pb2. py)
* These generated files help in loading, saving and accessing data  
* Since Protobuf  generates the pb2. py files, I used the files that are already generated from Ubuntu  
* This saved a couple of hours time( I would still give this step a try sometime soon)  
* Installed packages like opencv, matplotlib, jupyter  
* Faced many issues. Stack Overflow to the rescue!   
* Finally got object detection to work on Raspberry Pi  
* It is not as quick as the other platforms. But hey, this is one tiny amesome device!!  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/objectdetectionpi.png"/></p>   


**Read the blog** - [Engineering Safety with Uber's Real-Time ID Check](https://eng.uber.com/real-time-id-check/)     
* With real-time ID check, Uber ensures safety of the rider by authorising the driver  
* Uber uses Microsoft's Face API for both face detection and verification  
* Switching to a white UI from dark background gave a drastic improvement  
* In order to facilitate even low end devices, the detection is handled at backend  
* Tries to verify even with glasses on face  
* Prompts to remove glasses if face is not detected  with glasses  

**What to try next :**   
* Try detection on live camera feed   
* Try the new models released from TensorFlow   


