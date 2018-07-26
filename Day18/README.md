**Day 18 - 26th July, 2018:** Google's DeepDream   
* So what is DeepDream?   
* It is a program that takes an image as an input and gives another image as an output  
* Does it sound too simple to have a fancy name like DeepDream?  
* The output images are not just like the input images though  
* They look dream-like and the image below will give an idea about what that means  
* Does the output image look artistic, interesting and intriguing or random, unclear and hard to interpret?  
* It is really useful to understand how we got that as the output  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/deepdream.PNG"/></p>  


* Neural networks have a wide range of applications  
* Given enough examples and their labels, neural networks can learn from the examples  
* The learnings of the networks can be then used on unseen data/examples to predict their labels  
* From that perspective, it is clear what the inputs and outputs are  
* What about the black box that is involved?    
* How do the neural networks do what they do?   
* In between the input and the output, there are a number of hidden(powerful) layers   
* Each of these hidden layers learn some specific features/patterns in the input images  
* Understanding how each of those layers interpret and learn these patterns, will help in making the models better  
* This study of neural networks to understand how they interpret the input examples is called neural networks interpretation  
* This in itself is now being treated as a research field  
* Coming back to DeepDream, this program uses a neural network(GoogleNet) that is already trained on a large data  
* The idea behind this program is to let the network find any patterns in the input image which it has learnt from the training data 
* And enhance those patterns so that they resemble the objects the model thinks they belong to  
* This helps in understanding how the model has come up with the output label and what features led to the outcome  

**Some useful links:**  
* [Inceptionism: Going Deeper into Neural Networks](https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html)  
* [The Building Blocks of Interpretability](https://distill.pub/2018/building-blocks/)  
* [How Google Deep Dream works](https://computer.howstuffworks.com/google-deep-dream.htm)   

**Want to try this on some image?**  
* Here is the [link](https://github.com/theimgclist/100DaysOfMLCode/blob/master/notebooks/deepdream.ipynb) to the notebook with code from Google  
* Google's [Seedbank](https://tools.google.com/seedbank/) is a great resource for many other interesting Deep Learning projects  

**What to try next :**   
* Read more about face processing 
*  Explore TensorFlow and SeedBank
