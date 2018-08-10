**Day 26 - 5th Aug, 2018:** Normal Map  

* Texture maps are 2D images that are wrapped around or applied on an object/surface to make them look more realistic  
* They add more details and give an illusion of depth to the scenes in graphics  
* Normal map is one of the texture maps which is a variant of bump maps  
* Just like bump maps, normal maps add more details to object surfaces  
* These details can be structural which apply some structures on the surface  
* Normal maps when applied gives an illusion of depth/height on the surface   

<p><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/normalmap.png"/></p>  

* In the example above, the image on left without normal looks flat without any impression of depth or cracks between the bricks  
* When normal map is applied, the image gets transformed and looks more realistic with some impression of depth between the bricks  
* But how does a normal map look like?  

<p align="center"><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/normalmap_RGB.png"/></p> 

* Normal map looks like the above 2D image with blue being the major visible color and tints of red and green along the edges and corners 
* The above 2D image is created by using each pixel in it to store the information of direction of normal to that point  
* The RGB values of each pixel correspond to the X,Y,Z dimensions respectively  
* The regions shaded with blue mean that the normals point towards the Z direction, the green corners denote the normal direction towards Y axis and similarly the red tint on some of the edges represent the normal's direction towards X axis  
* Besides giving a sense of depth, using these normal directions the normal maps help in figuring out the geometry/shape of the scene/object  

**Some useful links:**  
* [https://learnopengl.com/Advanced-Lighting/Normal-Mapping]()  


