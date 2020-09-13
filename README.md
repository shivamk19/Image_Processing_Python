# Image_Processing_Python
Recognition of Images and Modifying Images using Python.
  
## Task 1
### 1. Image Rotation
**Original Input image**  
  ![**original image**](https://github.com/atharva1608/sra_ip_practice/blob/master/ImageRotation/rotate.png)  
    
 **Rotating it by 50 degree**  
  ![**rotated image**](https://github.com/atharva1608/sra_ip_practice/blob/master/ImageRotation/rotationofimageoutput1.png)
  
  ## Task 2
  ### 2. Applying Kernel
  Blurring and sharpening the image by using kernel(3x3 filters).
  |<img width="640" height="450" src="https://github.com/atharva1608/sra_ip_practice/blob/master/Applying_Kernels/blur.jpeg">|<img width="640" height="450" src="https://github.com/atharva1608/sra_ip_practice/blob/master/Applying_Kernels/filter.png">|
|:---:|:---:|

**Output**
|<img width="350" height="400" src="https://github.com/atharva1608/sra_ip_practice/blob/master/Applying_Kernels/outputblurimage.jpeg">|<img width="350" height="400" src="https://github.com/atharva1608/sra_ip_practice/blob/master/Applying_Kernels/outputblurimage1.jpeg">|<img width="350" height="400" src="https://github.com/atharva1608/sra_ip_practice/blob/master/Applying_Kernels/outputsharpenimage.png">|
|:---:|:---:|:---:|
|Gaussian Filter|Box Filter|Sharpen|

  
  ## Task 3
  ### 3. Edge Detection
  1. Vertical Edge Detection is done by using vertical filter(3x3).
  2. Horizongtal Edge Detction is done by using horizontal filter(3x3),
  3. Sobel Edge Detection was done by using two filters sobelx and sobely and applying on the given image.
   **Input Image**
  ![**input image**](https://github.com/atharva1608/sra_ip_practice/blob/master/Edge_detection/edge-detection.png)
  
  **Applying Sobel Edge Detector**
  ![**output image**](https://github.com/atharva1608/sra_ip_practice/blob/master/Edge_detection/outputedgedetectionsobel.png)
  4. Canny Edge Detection: It basically consists of five steps- 1) Noise Reduction 2)Gradient Calculation 3)Non-maximum suppression 4)Double Threshold 5)Edge   Tracking Hysteresis
  
  ## Task 4  
  Original Image                     |  Erosion                |  Dilation
:-------------------------:|:-------------------------:|:-------------------------:
<img width="320" height="220" src="https://github.com/shivamk19/Image_Processing_Python/blob/master/Morphological%20Transformation/morphological.png">|<img width="320" height="220" src="https://github.com/shivamk19/Image_Processing_Python/blob/master/Morphological%20Transformation/Erosion.png">|<img width="320" height="220" src="https://github.com/shivamk19/Image_Processing_Python/blob/master/Morphological%20Transformation/Dilation.jpg">
  
  ## Task 5
 Input Image                      |  Blue Ball Detected
:-------------------------:|:-------------------------:
<img width="540" height="400" src="https://github.com/shivamk19/Image_Processing_Python/blob/master/Masking/mask.jpg">|<img width="540" height="400" src="https://github.com/shivamk19/Image_Processing_Python/blob/master/Masking/Masked%20Image.jpg">
 
 ## Task 6
 Figure 1                      |  Figure 2
:-------------------------:|:-------------------------:
<img width="640" height="450" src="https://github.com/shivamk19/Image_Processing_Python/blob/master/ROI/roi.jpg">|<img width="640" height="450" src="https://github.com/shivamk19/Image_Processing_Python/blob/master/ROI/ROI%20ouput.jpeg">
