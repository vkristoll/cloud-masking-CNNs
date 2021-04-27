##Data pre-processing
# Import libraries
import os
import numpy as np
import tifffile as tiff

# Indicate the path to the training Sentinel-2 images (The images have been padded with "patch size/2" in x and y direction to retain the x-y size when producing the CNN cloud mask) 
directory = os.listdir('add path to the folder containing the training images')
os.chdir('add path to the folder containing the training images')  

# Sort directory
directory2=sorted(directory) 

#Create zero matrix to contain all training images
A1=np.zeros((16,1846,1846,13)) # (number of training images,x_size,y_size, number of bands)

c=0
for file in directory2:
        c=c+1
        im=tiff.imread(file)
        im13=im[:,:,0:13]
        im13b=im13/10000
        A1[c-1,:,:,:]=im13b 


# Indicate the path to the training ground-truth cloud masks (The images have been padded with "patch size/2") 
directory = os.listdir('add path to the folder containing the training ground-truth cloud masks')
os.chdir('add path to the folder containing the training ground-truth cloud masks')   

# Sort directory
directory3=sorted(directory)

# Create zero matrix to contain all training ground-truth cloud masks
A2=np.zeros((16,1846,1846)) # (number of  training ground-truth cloud masks,x_size,y_size)

c=0
for file in directory3:
   c=c+1
   im=tiff.imread(file)
   A2[c-1,:,:]=im     
   size=im.shape

# Indicate the path to the Sentinel-2 images of the test dataset (The images have been padded with "patch size/2" )
directory = os.listdir('add path to the folder containing the test images')
os.chdir('add path to the folder containing the test images')   

# Sort directory
directory2b=sorted(directory)

# Create zero matrix to contain all test images
A1b=np.zeros((21,1846,1846,13)) # (number of test images,x_size,y_size, number of bands)

c=0
for file in directory2b:
        c=c+1
        im=tiff.imread(file)
        im13=im[:,:,0:13]
        im13b=im13/10000
        A1b[c-1,:,:,:]=im13b


# Indicate the path to the ground-truth cloud masks of the test dataset (The images have been padded with "patch size/2")
directory = os.listdir('add path to the folder containing the test ground-truth cloud masks')
os.chdir('add path to the folder containing the test ground-truth cloud masks')   

# Sort directory
directory3b=sorted(directory)

####
# Create zero matrix to contain all test ground-truth cloud masks
A2b=np.zeros((21,1846,1846)) #(number of  test ground-truth cloud masks,x_size,y_size)

c=0
for file in directory3b:
   c=c+1
   im=tiff.imread(file)
   A2b[c-1,:,:]=im     
     

# ysize is used in the generation of the training and test patches
size=im.shape
xsize = size[1]   
ysize = size[0]

