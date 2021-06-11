#Downloading the data


#The ground truth cloud masks for the Sentinel-2 images  were downloaded from https://zenodo.org/record/1460961#.XvTC6JaxW8g
#The respective Sentinel-2 images were downloaded by using the sentinelsat package https://pypi.org/project/sentinelsat/ from https://scihub.copernicus.eu/dhus


#Downloading Sentinel-2 images

#Importing libraries
import os
from sentinelsat.sentinel import SentinelAPI

# connect to the API
api = SentinelAPI('user', 'password', 'https://scihub.copernicus.eu/dhus')

#directory: folder which contains a different folder for each cloud mask. This is a folder that already exists in the data downloaded from https://zenodo.org/record/1460961#.XvTC6JaxW8g

directory = os.listdir('/.../SENTINEL_2_reference_cloud_masks_Baetens_Hagolle/Reference_dataset')

#Sorting the directory according to the names of the folders  
directory2=sorted(directory)
size="number of files in the directory"

for i in range (size):
    #Create a variable that stores the name of each folder (i.e. name of the Sentinel-2 product of the image)
    name=directory2[i]
    #Adding the extension of the Sentinel-2 products
    name2= name + '.SAFE'
    #Search for the product
    product = api.query(filename=name2)
    #Download the product
    api.download_all(product)

#** If the product is not available, it will be available after a few hours. But it will be again unavailable after a day.
