#Calculating the evaluation metrics  

#Importing libraries
import os
import numpy as np
import tifffile as tiff
from sklearn.metrics import confusion_matrix
import time

#Creating functions for the evaluation metrics
def recall(confusion_matrix):
    col = confusion_matrix[:, 0]
    return confusion_matrix[0, 0] / col.sum()

def precision(confusion_matrix):
    row = confusion_matrix[0, :]
    return confusion_matrix[0, 0] / row.sum()

def fscore(confusion_matrix):
    col = confusion_matrix[:, 0]
    precision=confusion_matrix[0, 0] / col.sum()
    row = confusion_matrix[0, :]
    recall=confusion_matrix[0, 0] / row.sum()
    return 2*precision*recall/(precision+recall)

def accuracy(confusion_matrix):
    diagonal_sum = confusion_matrix.trace()
    sum_of_all_elements = confusion_matrix.sum()
    return diagonal_sum / sum_of_all_elements 


directory1= os.listdir('path to the folder with the ground truth cloud masks')
directory2= os.listdir('path to the folder with the cloud masks produced by the CNN')

directory1a= 'path to the folder with the ground truth cloud masks'
directory2a= 'path to the folder with the cloud masks produced by the CNN'

directory1b=sorted(directory1)
directory2b=sorted(directory2)

number_files="total number of files"

#Creating array to store the confusion matrix information
Conf_info=np.zeros(("total number of files",4))

#Creating array to store the information of the evaluation metrics
metrics=np.zeros(("total number of files + 1",4))

start_time = time.time()
for i in range(number_files):   

    print(" The repetition number is %s" %i)  
    print("--- %s seconds ---" % (time.time() - start_time))  

    #Read the first ground truth cloud mask 
    os.chdir(directory1a)
    gt_mask= tiff.imread(directory1b[i])
    size=1830*1830
    #Reshape the ground truth cloud mask
    gt_mask2=np.reshape(gt_mask,(size,1)) 
  
    #Read first CNN cloud mask
    os.chdir(directory2a)
    CNN_mask=tiff.imread(directory2b[i])
    #Reshape the ground truth cloud mask
    CNN_mask2=np.reshape(CNN_mask,(size,1)) 

    #Calculate the confusion matrix
    conf_m=confusion_matrix(gt_mask2, CNN_mask2,labels=[0,255]) 
    
    #Store the confusion matrix information
    Conf_info[i,0]=conf_m[0,0]
    Conf_info[i,1]=conf_m[0,1]
    Conf_info[i,2]=conf_m[1,0]
    Conf_info[i,3]=conf_m[1,1]
    
    #Store the information of the evaluation metrics
    acc=accuracy(conf_m)
    
    metrics[i,0]=acc
    metrics[i,1]=precision(conf_m)
    metrics[i,2]=recall(conf_m)
    metrics[i,3]=fscore(conf_m)
    print(" The accuracy number is %s" %metrics[i,0])     
    
#Calculate the average values for the evaluation metrics    
acc_all=np.mean(metrics[0:"total number of files + 1",0])
prec_all=np.mean(metrics[0:"total number of files + 1",1])
recall_all=np.mean(metrics[0:"total number of files + 1",2])
fscore_all=np.mean(metrics[0:"total number of files + 1",3])

#Store the average values for the evaluation metrics
metrics["total number of files",0]=acc_all
metrics["total number of files",1]=prec_all
metrics["total number of files",2]=recall_all
metrics["total number of files",3]=fscore_all

#Save the confusion matrix and the evaluation metrics
np.savetxt("confusion_matrix.csv", Conf_info, delimiter=',', header=" #TP,  #FP,  #FN,  #TN  ",fmt='%10.0f')
np.savetxt("metrics.csv", metrics, delimiter=',', header=" #accuracy,  #precision,  #recall, #fscore ",fmt='%10.4f')           
        
      
    
