import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

def ratioBW(fileName):
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

    
    
def ratioBWImported(fileName):

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



'''
fileName1 = input('fileName1: ')
fileName2 = input('fileName2: ')
fileName3 = input('fileName3: ')

print(ratioBWImported(fileName1) + ratioBWImported(fileName2))
print(ratioBW(fileName3))

print(((ratioBWImported(fileName1)[0]+ratioBWImported(fileName2)[0])/ratioBW(fileName3)[0])*100)
'''


