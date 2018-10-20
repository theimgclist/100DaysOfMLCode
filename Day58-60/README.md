**Day 58 to 60 - 10th to 12th Sept, 2018:** Face Image Normalization(Paper)

* Just a decade ago, the amount of biometric data available through any sources is far less than what we have now  
* Be it phones that now have biometric modes of verification(like fingerprint, face recognition) or many other places like airports that are now using identity recognition to provide hassle free experience, they all are using biometric data  
* These wide applications of biometric data also call for an accepted specification that helps in making the process smooth,safe and fool proof  
* In most cases, the facial identity of a person is verified against a document proof
* The extent to which the process of automating this task depends a lot on the quality of the identity's face on the document
* The International Civil Aviation Organization provides specifications which help in classifying images as suitable or not for a document proof  
* Depending on parameters like deviation from frontal pose,eyes-open,mouth-closed, eyes looking away, we can decide whether the image meets the criteria

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/facenorm.png"/></p>

* In the Tokenization phase, face detection is done on the input image  
* Even when multiple faces are detected, the model should be robust enough to detect the right face  
* AdaBoost is used for robust face detection  
* For every detected face, using the bounding box the actual facial components, mouth, eyes are located using AdaBoost classifier  
* After tokenization, the image then goes through few classifications for each of these parameters - deviation from frontal pose, eyes-open, mouth-closed and eyes looking away  
* The outputs of each of these classifiers help in decision making  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/icaospec.png"/></p>

* [(PDF) Face image normalization and expression/pose validation for the analysis of machine readable travel documents](https://www.researchgate.net/publication/282732909_Face_image_normalization_and_expressionpose_validation_for_the_analysis_of_machine_readable_travel_documents)

