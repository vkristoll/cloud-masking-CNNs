#CNN training

#Importing libraries
import time
import keras 
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import model_from_json
from keras.layers import LeakyReLU
from keras.layers import BatchNormalization
from keras.layers import Dropout

# Initialising the CNN
classifier = Sequential()

# Adding input layer and first convolutional layer
classifier.add(Conv2D(8, (3, 3), input_shape = (16, 16, 13),activation='relu',padding='same'))
#classifier.add(BatchNormalization(momentum=0.0))
#classifier.add(LeakyReLU(alpha=0.3))

# Adding first pooling layer
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding second convolutional layer
classifier.add(Conv2D(8, (3, 3), activation='relu',padding='same'))
#classifier.add(BatchNormalization(momentum=0.0))
#classifier.add(LeakyReLU(alpha=0.3))

# Adding second pooling layer
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding third convolutional layer
classifier.add(Conv2D(8, (3, 3), activation='relu',padding='same'))
#classifier.add(BatchNormalization(momentum=0.0))
#classifier.add(LeakyReLU(alpha=0.3))

# Adding third pooling layer
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Flattening
classifier.add(Flatten())

# Adding fully connected hidden layer
classifier.add(Dense(units = 50, activation = 'relu'))
classifier.add(Dropout(rate=0.3))

# Adding second hidden layer
classifier.add(Dense(units = 50, activation = 'relu'))
classifier.add(Dropout(rate=0.3))

# Adding the output layer
classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

train_steps=10000
#checkpoint
#The use of the checkpoint allows to save weights after every epoch in an .hdf5 file
filepath="weights.{epoch:02d}.hdf5"
checkpoint=keras.callbacks.ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=False, save_weights_only=True, mode='max')
callbacks_list = [checkpoint]

start_time = time.time()

# Fitting the CNN to the Training set

history=classifier.fit_generator(image_generator(), steps_per_epoch=train_steps,  validation_data = image_generatorb(), validation_steps = train_steps, epochs=30,callbacks=callbacks_list ) 

print("--- %s seconds ---" % (time.time() - start_time))

# summarize history for accuracy

# list all data in history
print(history.history.keys())

# Print and save the accuracy plot
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='lower right')
# Major ticks
ax=plt.gca()
ax.set_xticks(np.arange(0, 30, 2))
## Labels for major ticks
ax.set_xticklabels(np.arange(1, 31, 2));
plt.savefig("figure name",dpi=300)
plt.show()


# If the checkpoint was not used, the final weights can be saved and then loaded at a later time as shown below:
#classifier.save_weights("weights.h5")
#classifier.load_weights("weights.h5") 
