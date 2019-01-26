import numpy as np
from PIL import Image

def ratioBW(fileName):
    #converting image to array
    img = Image.open(fileName).convert('1')
    imgArr = np.array(img);
    
    #making it 1D
    flatArr = imgArr.ravel()
    
    #calculating ratios
    total = len(flatArr)
    black = np.sum(flatArr)
    white = total - black
     
    #Return [Black, White, Total]
    return [black, white, total]

#fileName = input('fileName: ')

#print(ratioBW(fileName))



