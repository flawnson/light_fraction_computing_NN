# light_fraction_computing_NN
## Overview
Project Monochrome: A software built in Python capable of detecting the shade, shape, and area of elements in a given image. This is our Deltahacks 2019 project. Initially the challenge appears to be suitable for a machine learning application, but upon investigation, the use of OpenCv and Scilib-image was determined to be far more effective for computing the fraction of light vs dark pixels in an image of irregular polygons and calculating the size of said polygons.

Officially, there where 5 possible tiers/targets
1. Determine the fraction of light vs dark pixels
2. Same as Target 1 but with added noice in the images
3. Same as Target 1 and 2 but with added gradint in the images
4. Determine the average surface area of the polyogons in the image
5. Create a histogram (Gaussian DIstribution) of target 4

Our team of 4 consisted of @liryan914, @wangwillson1, @agosh-saini, and @flawnson. Ryan Li was in charge of research, specifically in the types of thresholding (OTSU) and laplacians. Willson was in charge of front end development, and suceeded in building a framework that would bridge the algorithm to a user friendly image upload webpage. Agosh and myself (Flawnson) used OpenCV, Sciplot, and Matplotlib to build the algorithm.

## Challenges
Initial challenges involved thresholding, specifically to solve the problem of image gradients presented by Target 3. There was some difficulty in choosing between edge vs shape detection when attempting to solve Target 4.

## Sample Images
()

## Test results
Target 1 tests acheived nearly perfect accuracy, after thresholding and binarization
Target 2 tests acheived 98% accuracy, after thresholding, binarization, and noise reduction (using laplacians kernels)
Target 3 tests acheived 82% accuracy, after thresholding, binarization, noise reduction, additional contrast thresholding, and inversing
Target 4 tests where not directly measured, but was certainly accurate within a relatively small degree of error
Target 5 tests relied on the results of Target 4, thus has the same accuracy and rate of error.

## Applications
Project Monochrome has potential to be applied accross various industries where there is a need for better image analysis. Such applications and industries include:

* Analyzing CT scans for cancer detection and determination of malignance or benign
* Increased accuracy in object detection for thermal imaging in warfare and defence
* Use in X-ray technology to help doctors determine the nature of an injury, ranging from a break or fracture to determining osteopenia
* Use in material science, where such image analysis would be useful in determining the strength, flexibility, etc. of a given material
* Use in microscopy, where biological changes in cells could be commercially detected instead of manually.

## Future
Project monochrome has no use for an A.I, but results may have been better, for example, had we implemented YOLO object detection to Targets 4 and 5, or perhaps a supervised learning technique. There is a high probability such an A.I would detect objects better than our OpenCV-based algorithm. As such, this is a potential space for improvement.

While the potential applciations are numerous, we have yet to test Project Monochrome on images beyond that of last two applications (materials and organic material). This may be a reference for future work.

Upwards and onwards, always and only! :rocket:
