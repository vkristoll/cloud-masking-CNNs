#This function generates test patches (size: 13x16x16) and the respective value of the  test cloud mask for the central pixel

# xsize, ysize, A1b, A2b are defined in "data_preprocessing.py"

def image_generatorb():  
    
  while True:
    
   randomindex=np.random.choice(ysize-16)
   randomindex2=np.random.choice(21)
      
   a=ysize-16
   X= np.zeros((a,16,16,13))
   c=0     
   for i in range(0, xsize-16, 1):
        c=c+1
        X[c-1,:,:,:]= A1b[randomindex2,randomindex:randomindex+16,i:i+16,:]      

       
   y= np.zeros((a,16,16))       
   c=0        
   for i in range(0, xsize-16, 1):
       c=c+1
       y[c-1,:,:]= A2b[randomindex2,randomindex:randomindex+16,i:i+16]       

   y2=np.zeros((a,1))

   for i in range(a):
       y2[i,0]=y[i,8,8] 
       
   for i in range(a):
      if y2[i,0]==255:
          y2[i,0]=1     
        
   yield (X, y2) 
