# Adding padding of 8 pixels in the x and y direction

# Import libraries

import os
import gdal
import numpy as np
directory = os.listdir('add path to the folder containing the images')
os.chdir('add path to the folder containing the images')

# Sort directory
directory2=sorted(directory)

for file in directory2:
    ds=gdal.Open(file) 
    geotransform= ds.GetGeoTransform()
    projection=ds.GetProjection()
    A=np.zeros((13,1846,1846))
    for i in range (13):    
        a=np.array(ds.GetRasterBand(i+1).ReadAsArray())
        A[i,8:1838,8:1838]=a

    xSize=1846
    ySize=1846
    
    file_name = os.path.basename(file)
    new_filename = file_name.split('.')[0]     
    target_layer=new_filename +'pad8'+'.tif'
    driver= gdal.GetDriverByName('GTiff')
    target_ds = driver.Create(target_layer, xSize, ySize, bands=13, eType=gdal.GDT_Float32)
    target_ds.SetGeoTransform(geotransform)
    target_ds.SetProjection(projection) 
    
    for i in range(13):
        outBand = target_ds.GetRasterBand(i+1)
        outBand.WriteArray(A[i,:,:])


    # Close raster file
    target_ds= None






