# CNN predictions

#Import libraries
import os
import numpy as np
import tifffile as tiff
import time

# Indicate the path to the training or test Sentinel-2 images
directory = os.listdir('add path to the folder containing the train or test images')
os.chdir('add path to the folder containing the train or test images')   

# Sort directory
directory2=sorted(directory)

# Read image one by one and save the predicted cloud mask
start_time = time.time()
number=0
for file in directory2: 
    number=number+1
    im=tiff.imread(file)
    im13=im[:,:,0:13]
    im13b=im13/10000
    size=im.shape
    xsize = size[1]
    ysize = size[0]
    a=ysize-16
    X= np.zeros((a,16,16,13))    
    
    l=[]   
    c=0
    for j in range(0, ysize-16,1):    
      for i in range(0, xsize-16,1):
        c=c+1
        X[c-1,:,:,:]= im13b[j:j+16,i:i+16,:]     

      c=0
      Cls=classifier.predict(X)
      l.append(Cls)      

    M=np.zeros((1830,1830)) ## image size without padding
    for i in range(1830):   
        M[i,:]=l[i].reshape(1,-1)

    for i in range(1830):
        for j in range(1830):
            if M[i,j]==0.5 or M[i,j]<0.5:
                M[i,j]=0
            elif M[i,j]>0.5:
                M[i,j]=255 
                
    M2=np.uint8(M)

    file_name = os.path.basename(file)
    new_filename = file_name.split('.')[0] 

    tiff.imsave(new_filename + 'pred.tif', M2)
    print("--- %s seconds ---" % (time.time() - start_time))
    print('finished number %s' %number)



