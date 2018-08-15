**Day 34 - 13th Aug, 2018:** L1 Norm, L2 Norm, Max Norm   

* Vector norm is nothing but the length or magnitude of the vector  
* Just like co-ordinating systems, vectors are quite useful in many fields  
* In Machine Learning too, we try to represent an example/sample with n factors/features in some N-dimensional space   
* This is very essential for representation learning as the position of each example with respect to its position helps in inference    
* Knowing vector magnitude is helpful in a number of ways    
* There are different ways to derive and express the magnitude of a vector  
* L1 norm, L2 norm and Max norm are three ways to calculate vector magnitude  
* These can be used for regularization or as loss functions by the learning models  

**L1 Norm** :  
* L1 norm is also called as least absolute error  
* This can be calculated by simply adding the different coordinate values together(when we assume the other point is at the origin)    
```Python  
# l1 norm of a vector
from numpy import array
from numpy.linalg import norm
a = array([1, 2, 3])
print(a)
l1 = norm(a, 1)
print(l1)  
```  

* When used as a loss function, it caluculates the sum of differences between actual and predicted values for every sample  
* This way it gives a measure of how good or bad the machine learning model performed  
 
<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/l1loss.PNG"/></p>   

**L2 Norm** :  
* It is also called least squares  
* In this norm or loss function, instead of sum of differences, the sum of squares of differences is taken to measure the vector distance or the loss  
* This is how we can calulate L2 norm using Python :  
```Python  
# l2 norm of a vector
from numpy import array
from numpy.linalg import norm
a = array([1, 2, 3])
print(a)
l2 = norm(a)
print(l2)  
```  
* As a loss function, it calculates the sum of squares of differences between the actual and predicted values  

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/l2loss.PNG"/></p>    

**Max Norm** :  
* This is the simplest of the three  
* As the name suggests, max norm returns the maximum of all the values  
* It can be calculated using the below code :  
```Python  
# max norm of a vector
from numpy import inf
from numpy import array
from numpy.linalg import norm
a = array([1, 2, 3])
print(a)
maxnorm = norm(a, inf)
print(maxnorm)  
```  

**How to choose between L1 and L2 norm?**  
* The below table summarizes the differences between L1 and L2 norm  
<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/l1vsl2.PNG"/></p> 
  	

**Some Useful Links :**  
* [Differences between the L1-norm and the L2-norm (Least Absolute Deviations and Least Squares)](http://www.chioka.in/differences-between-the-l1-norm-and-the-l2-norm-least-absolute-deviations-and-least-squares/)
* [Gentle Introduction to Vector Norms in Machine Learning](https://machinelearningmastery.com/vector-norms-machine-learning/)

