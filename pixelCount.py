import numpy as np
from PIL import Image
import os

def ratioBW(fileName):
    #checking if file exists
    if os.path.isfile('./'+ fileName) == True:
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
    else:
        #returns if file Does not exist in directory
        return False
    


#fileName = input('fileName: ')

#print(ratioBW(fileName))



