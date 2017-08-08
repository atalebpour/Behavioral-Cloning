import csv
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Dropout, Activation, Cropping2D
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D

lines = []
with open ('./data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)

images = []
steering_measurements = []
correction = 0.2
for line in lines:
    source_path = line[0]
    filename = source_path.split('/')[-1]
    current_path = './data/IMG/' + filename
    image = cv2.imread(current_path)
    images.append(image)
    steering_measurement = float(line[3])
    steering_measurements.append(steering_measurement)	
    augmented_image = cv2.flip(image, 1)
    images.append(augmented_image)
    augmented_steering_measurement = steering_measurement * -1.0
    steering_measurements.append(augmented_steering_measurement)


X_train = np.array(images)
y_train = np.array(steering_measurements)

model = Sequential()
model.add(Lambda (lambda x: x / 225.0 - 0.5,  input_shape = (160, 320, 3)))
model.add(Cropping2D(cropping = ((70, 25),(0, 0))))
model.add(Convolution2D(24, 5, 5, subsample=(2,2), activation='relu'))
model.add(MaxPooling2D(pool_size=(1, 1)))
model.add(Convolution2D(36, 5, 5, subsample=(2,2), activation='relu'))
model.add(Convolution2D(48, 5, 5, subsample=(2,2), activation='relu'))
model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(Dropout(0.25))
model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(Convolution2D(128, 1, 1, activation='relu'))
model.add(Convolution2D(128, 1, 1, activation='relu'))
model.add(Flatten())
#model.add(Dense(100))
#model.add(Dense(50))
#model.add(Dense(10))

#model.add(Dense(200))
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, batch_size=128, nb_epoch=2, validation_split=0.2, shuffle=True)

model.save('model.h5')
