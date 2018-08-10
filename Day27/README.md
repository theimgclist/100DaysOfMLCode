**Day 27 - 6th Aug, 2018:** Albedo Map  

**What are albedo maps?**  
* It took some time to understand normal maps, especially how the blue/green/red shades are painted in the 2D normal map    
* ALbedo maps on the other hand are easy to understand    
* Since textures are the images applied on the surface of a mesh/object which are subjected to different light conditions, it is best to remove any existing highligts,shadows, light elements from the 2D textures before applying them to the surface so that the light components can be rendered accordingly in the scene  
* Albedo maps are like diffuse maps from which the highlights, shadows and light patches are removed    
* This gives an even/homogeneous layer with only the color component  

<p align="center"><img src="https://raw.githubusercontent.com/theimgclist/100DaysOfMLCode/master/images/albedomap.png"/></p>  

* Albedo map along with the normal map and lighting can then be used by the shader to reconstruct the image   
* Since the rendering algorithm/engine takes care of lighting the scene/image being rendered, albedo maps make it easier by removing the unwanted highlights/shadows  

**How to create an albedo map in Photoshop?**  
* Saturate the image - Removes the color  
* Invert the saturated image - Light pixels get darker and dark pixels get lighter  
* Apply Soft Light blend mode to get the Albedo Map  

**Some useful links:**    
* [https://www.cgdirector.com/albedo-map/]()  


