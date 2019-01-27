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
        white = np.sum(flatArr)
        black = total - white
         
        #Return [white, black, total]
        return [white, black, total]    
    else:
        #returns if file Does not exist in directory
        return False
    
    
def ratioBWImported(fileName):
    #checking if file exists
    if os.path.isfile('./'+ fileName) == True:
        #converting image to array
        img = Image.open(fileName).convert('1')
        imgArr = np.array(img);
        
        #making it 1D
        flatArr = imgArr.ravel()
        
        #calculating ratios
        total = len(flatArr) - 53369
        white = np.sum(flatArr) - 53369
        black = total - white
         
        #Return [white, black, total]
        return [white, black, total]    
    else:
        #returns if file Does not exist in directory
        return False
    

'''
fileName1 = input('fileName1: ')
fileName2 = input('fileName2: ')
fileName3 = input('fileName3: ')

print(ratioBWImported(fileName1) + ratioBWImported(fileName2))
print(ratioBW(fileName3))

print(((ratioBWImported(fileName1)[0]+ratioBWImported(fileName2)[0])/ratioBW(fileName3)[0])*100)
'''


