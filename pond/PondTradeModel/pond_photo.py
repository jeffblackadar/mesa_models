# import the necessary packages
# Credit to: Adrian Rosebrock https://www.pyimagesearch.com/
#from imutils import paths
from matplotlib import pyplot
import argparse
import sys
import cv2
import os

import shutil
from pathlib import Path
img_local_folder = "C:\\Users\\jblackad\\mesa\\src\\mesa\\charcoal\\pond\\PondTradeModel\\"
path = Path(img_local_folder)
os.chdir(path)
# 192X135 is used since it's a multiple of 64X45. 
img_file_name = "med_bw.png"
hash_image = cv2.imread(img_file_name)

# if the image is None then we could not load it from disk (so skip it)
if not hash_image is None:
    # convert the image to grayscale and compute the hash
    #pyplot.imshow(hash_image)    
    #pyplot.show()

    hash_image = cv2.cvtColor(hash_image, cv2.COLOR_BGR2GRAY)
    pyplot.imshow(hash_image,cmap='gray')    
    #pyplot.show()

    # resize the input image to 64 pixels wide and 30 high.
   
    resized = cv2.resize(hash_image, (100,100))
    pyplot.imshow(resized,cmap='gray')
    pyplot.show()
    
    #convert the grayscale to black and white using a threshold of 92
    (thresh, blackAndWhiteImage) = cv2.threshold(resized, 92, 255, cv2.THRESH_BINARY)
    print(blackAndWhiteImage)
    pyplot.imshow(blackAndWhiteImage,cmap='gray')
    pyplot.show()
    matrix = ""
    for row_count in range(0,100,1):
        row = "["
        comma = ""
        for col_count in range(0,100,1):
            #[0,0,1,0,1,1],
            if(blackAndWhiteImage[row_count,col_count]==255):
                row = row + comma + "1"
            else:
                row = row + comma + "0"
            comma = ","
            row = row
        matrix = matrix + row + "],\n"
    print(matrix)

else:
    print("no image.")