**Day 55 to 57 - 6th Sept to 8th Sept, 2018:** FaceNet- Unified Embeddings(Paper)

* There are tons of papers on face processing, alignment, reconstruction and recognition    
* I read few of them as part of the research project on face reconstruction   
* [FaceNet](https://arxiv.org/abs/1503.03832) is a very informative paper for anyone interested in face embeddings and tasks like face verification and recognition that make use of embeddings  
* Given a human face image, the FaceNet model gives out its embedding  
* Embedding is nothing but a vector(a collection of numbers) of size 128 or 256 or 512  
* Since the vector is high dimensional, it gives the face representation which differs from person to person  
* Using the Euclidean distance between the embeddings of any two faces, we can conclude if it's the same person or not  
* The decision is made considering a threshold value  
* If the Euclidean distance between any two face embeddings is greater than the threshold, it possibly means there is no match, otherwise a match  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/facenet.png"/></p>

* The model is trained from data which had 100-200M face thumbnails collected from 8M identities
* The size of each of these images are from 96 X 96 to 256 X 256  
* Triplet loss function(contrastive loss function) is used  
* Triplet is a collection of 3 face images, with two of them being from the same person and the third from a different identity  
* This way the model tries to learn to separate identities by mapping similar faces to closer Euclidean spaces and different ones afar  
* It is observed that as the image quality and size increase, the validation score has increased  
* Also, the best validation score is obtained when the embedding vector is 128D, followed by 256, 64 and 512  
* While 128 is the optimal embedding dimension, low dimensional embeddings can be used for mobiles and low computation devices  
