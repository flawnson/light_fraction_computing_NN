%pylab inline
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import os
import matplotlib.patches as mpatches
from skimage import data
from skimage.filters import threshold_triangle
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb


def labelsInv(path):
  imagePath = path
  image = cv.imread(imagePath, 0)
  ret, image = cv.threshold(image, 0, 255, cv.THRESH_TOZERO_INV + cv.THRESH_OTSU )

  #Track labels
  numLabel = 0
  labelRegion = []
  
  # apply threshold
  thresh = threshold_mean(image)
  bw = closing(image > thresh, square(3))

  # remove artifacts connected to image border
  cleared = clear_border(bw)

  # label image regions
  label_image = label(cleared)
  image_label_overlay = label2rgb(label_image, image = image)

  fig, ax = plt.subplots(figsize = (10, 6))
  ax.imshow(image_label_overlay)

  for region in regionprops(label_image):
      # take regions with large enough areas
      if region.area >= 100:
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill = False, edgecolor = 'red', linewidth = 2)
        ax.add_patch(rect)

        labelRegion.append(region.area)
        numLabel = numLabel + 1
        
  ax.set_axis_off()
  plt.tight_layout()
  plt.show()

  return [numLabel, labelRegion]
  
  print(numLabel)
  
def labels(path):
  imagePath = path
  image = cv.imread(imagePath, 0)

  #Track labels
  labelRegion = []
  numLabel = 0
  
  # apply threshold
  thresh = threshold_mean(image)
  bw = closing(image > thresh, square(3))

  # remove artifacts connected to image border
  cleared = clear_border(bw)

  # label image regions
  label_image = label(cleared)
  image_label_overlay = label2rgb(label_image, image = image)

  fig, ax = plt.subplots(figsize = (10, 6))
  ax.imshow(image_label_overlay)

  for region in regionprops(label_image):
      # take regions with large enough areas
      if region.area >= 100:
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill = False, edgecolor = 'red', linewidth = 2)
        ax.add_patch(rect)

        labelRegion.append(region.area)
        numLabel = numLabel + 1
        
  ax.set_axis_off()
  plt.tight_layout()
  plt.show()

  return [numLabel, labelRegion]
   
def avgSize(numGrain):
  avgSize = 78400 / numGrain
  
  r = math.sqrt(avgSize / pi)
  surfaceArea = 4 * pi * r * r
  
  return [r * 2, avgSize, surfaceArea]

def histogram(label, labelInv):
  arr = label + labelInv
  arrArea = []
  
  for i in range(len(arr)):
      r = math.sqrt(arr[i] / pi)
      surfaceArea = 4 * pi * r * r
      arrArea.append(surfaceArea)
      
  arrArea = np.array(arrArea)    
  plt.hist(arrArea, bins = 'auto')
  plt.title('Surface Areas of Grains')
  plt.xlabel('Area in Pixels')
  plt.ylabel('Number of Grains')
  plt.show()

def main(filename):

    img = cv.imread(filename, 0)
    
    th = 0
    max_val = 255
    
    #for challenge 3 pre preparing
    ret, o6 = cv.threshold(img, th, max_val, cv.THRESH_BINARY + cv.THRESH_OTSU )
    ret, o7 = cv.threshold(img, th, max_val, cv.THRESH_BINARY_INV + cv.THRESH_OTSU )
    
    output = [o6, o7]

        
    
    for i in range(len(output)):
        plt.subplot(2, 4, i + 1)
        plt.imshow(output[i], cmap = 'gray')
        plt.xticks([])
        plt.yticks([])
        plt.savefig('my' + str(i) + '.png', dpi = 300, pad_inches = None, bbox_inches = 'tight')
    plt.show() 

if __name__ == "__main__":
    main('bb.png')