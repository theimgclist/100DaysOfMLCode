**Day 8 - 14th July, 2018:** Tried training on new dataset  
* Training TensorFlow Object Detection on a new API needs few changes to be done  
* Followed the instructions and made the necessary configuration changes  
* Faced few issues which I was able to resolve using GitHub Issues  
* All this took sometime  
* When training did start, there was OOM error  
* OOM is out of memory error  
* Due to computational constraints which come with laptop without GPU     

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/oom.png"/></p>   
 
* I first thought I should try running it on Colab, since it provides GPU    
* Before that I wanted to try if I can still do the training locally    
* The batch size was set to 24    
* Reducing the batch size will help when running on limited computation    
* I changed the batch size from 24 to 12   
* And it worked, training started   
* The trade off is that with reduced batch size, it takes more time to train    
* It has been close to an hour now since the training started    
* The loss has come down from 30 when the training started to 3 right now  
* It might take some more time to further reduce the loss    

**What to try next :**  
* Train the model till the loss is reduced    
* Try the training on Colab  

